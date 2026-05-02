# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import win32gui, win32con
import time
import pyautogui
import numpy as np
from PIL import Image, ImageDraw

pyautogui.PAUSE = 0.3
EDGE_HWND = 0x1509c0

win32gui.ShowWindow(EDGE_HWND, win32con.SW_RESTORE)
win32gui.SetForegroundWindow(EDGE_HWND)
time.sleep(0.3)

# Open dropdown
print("Opening type selector dropdown...")
pyautogui.click(750, 600)
time.sleep(0.4)
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('space')
time.sleep(1.0)

img = pyautogui.screenshot()
arr = np.array(img)
r, g, b = arr[450, 700, :3]
alive = r > 240 and g > 240 and b > 240
print(f"Dropdown open: {alive}")

if alive:
    # Ultra-precise zoom: crop JUST the left panel dropdown area
    # Left panel is x=215-514, y=380-540 (where dropdown items should be)
    zoom = img.crop((215, 380, 520, 550))
    draw = ImageDraw.Draw(zoom)
    # Fine grid every 10px with screen coordinate labels
    for x in range(0, zoom.width, 10):
        col = 'red' if x % 50 == 0 else 'pink'
        draw.line([(x,0),(x,zoom.height)], fill=col, width=1)
        if x % 20 == 0:
            draw.text((x+1,0), str(x+215), fill='red')
    for y in range(0, zoom.height, 10):
        col = 'blue' if y % 50 == 0 else 'lightblue'
        draw.line([(0,y),(zoom.width,y)], fill=col, width=1)
        if y % 20 == 0:
            draw.text((0,y+1), str(y+380), fill='blue')
    zoom.resize((zoom.width*3, zoom.height*3)).save(
        r'C:\claude\personal-website\screenshots\dropdown_precise.png')
    print("Saved dropdown_precise.png - will read to find exact coordinates")

    # Also try: scan each row of pixels to find the white/highlighted item rows
    # White rows = item backgrounds in dropdown
    region = np.array(img)[380:550, 215:515, :]
    print("\nBrightness scan (left panel, y=380-550):")
    for y in range(0, 170, 5):
        row = region[y, 20:200, :]  # sample columns 235-415 screen
        avg = row.mean(axis=0)
        print(f"  screen y={y+380}: RGB avg = ({avg[0]:.0f}, {avg[1]:.0f}, {avg[2]:.0f})")
