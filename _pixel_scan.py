# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import win32gui, win32con
import time
import pyautogui
import numpy as np
from PIL import Image, ImageDraw

pyautogui.PAUSE = 0.2
EDGE_HWND = 0x1509c0

win32gui.ShowWindow(EDGE_HWND, win32con.SW_RESTORE)
win32gui.SetForegroundWindow(EDGE_HWND)
time.sleep(0.3)

img = pyautogui.screenshot()
arr = np.array(img)

# Sample pixels at specific x positions, scanning down from y=300
# to find where the gray overlay ends and dialog starts
# Modal overlay = semi-transparent dark gray over white editor
# The gray overlay region will have R≈G≈B≈180-220 (dimmed white)
# Pure dialog white = R=G=B=255

print("Scanning pixels at different x positions:")
for test_x in [400, 500, 600, 700, 800, 900, 1000, 1100, 1200]:
    # Find first pure white at this x (moving down from y=300)
    for y in range(280, 1100, 5):
        r, g, b = arr[y, test_x, :3]
        if r > 252 and g > 252 and b > 252:
            print(f"  x={test_x}: first white at y={y}")
            break
    else:
        print(f"  x={test_x}: no pure white found")

print()
# Also scan horizontally at y=600 (middle of screen) to find dialog edges
print("Horizontal scan at y=600:")
prev_is_white = False
transitions = []
for x in range(100, 1500, 5):
    r, g, b = arr[600, x, :3]
    is_white = r > 250 and g > 250 and b > 250
    if is_white != prev_is_white:
        transitions.append((x, 'white' if is_white else 'non-white'))
        prev_is_white = is_white
print(f"  Transitions: {transitions[:10]}")

# Sample key pixel values at the region where dialog likely is
print()
print("Sample pixel values around expected dialog area:")
for y in range(320, 380, 10):
    row_vals = []
    for x in range(200, 1200, 100):
        r, g, b = arr[y, x, :3]
        row_vals.append(f"({r},{g},{b})")
    print(f"  y={y}: {' '.join(row_vals)}")
