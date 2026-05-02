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

# Find dialog left edge precisely by scanning at y=500 (mid dialog)
print("Horizontal scan at y=500 (looking for dialog left edge):")
for x in range(100, 600, 5):
    r, g, b = arr[500, x, :3]
    if r > 250 and g > 250 and b > 250:
        print(f"  First white at x={x}, y=500")
        break

# Find dialog top precisely
print("Vertical scan at x=600 (looking for dialog top):")
for y in range(280, 450, 2):
    r, g, b = arr[y, 600, :3]
    print(f"  y={y}: ({r},{g},{b})")
    if r > 250 and g > 250 and b > 250:
        print(f"  -> First white at y={y}, x=600")
        break

# Scan a wider range at y=500 to find both edges
print("\nFull scan at y=500 (all transitions):")
prev = None
for x in range(50, 1600, 5):
    r, g, b = arr[500, x, :3]
    is_white = r > 240 and g > 240 and b > 240
    if prev is not None and is_white != prev:
        print(f"  x={x}: {'→white' if is_white else '→dark'}, pixel=({r},{g},{b})")
    prev = is_white

# Also find bottom of dialog
print("\nVertical scan at x=600 looking for dialog bottom:")
in_dialog = False
for y in range(300, 1200, 2):
    r, g, b = arr[y, 600, :3]
    is_white = r > 240 and g > 240 and b > 240
    if not in_dialog and is_white:
        print(f"  Dialog top at y={y}")
        in_dialog = True
    elif in_dialog and not is_white:
        print(f"  Dialog bottom at y={y}")
        break
