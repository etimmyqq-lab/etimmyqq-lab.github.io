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
time.sleep(0.4)

# Re-open deployment dialog
pyautogui.click(1240, 375)
time.sleep(1.2)
pyautogui.click(1210, 435)
time.sleep(2.5)

# Immediately scan pixel colors
img = pyautogui.screenshot()
arr = np.array(img)

print("=== DIALOG OPEN - Pixel scan ===")
print("Vertical scan at x=600:")
for y in range(280, 600, 5):
    r, g, b = arr[y, 600, :3]
    brightness = int((int(r)+int(g)+int(b))/3)
    marker = " <-- DARK OVERLAY" if brightness < 150 else (" <-- DIALOG WHITE" if brightness > 240 else "")
    print(f"  y={y}: ({r},{g},{b}) brightness={brightness}{marker}")

print()
print("Horizontal scan at y=450:")
for x in range(100, 1400, 20):
    r, g, b = arr[450, x, :3]
    brightness = int((int(r)+int(g)+int(b))/3)
    if brightness < 150:
        print(f"  x={x}: DARK ({r},{g},{b})")
    elif brightness > 240:
        pass  # skip pure white
    else:
        print(f"  x={x}: GRAY ({r},{g},{b})")

# Find transitions at y=450
print("\nTransitions at y=450:")
prev_bright = None
for x in range(100, 1400, 2):
    r, g, b = arr[450, x, :3]
    bright = int((int(r)+int(g)+int(b))/3)
    state = 'white' if bright > 240 else ('dark' if bright < 150 else 'gray')
    if state != prev_bright:
        print(f"  x={x}: → {state} ({r},{g},{b})")
        prev_bright = state
