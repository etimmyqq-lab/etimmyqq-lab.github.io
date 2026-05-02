# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import win32gui, win32con
import time
import pyautogui
import numpy as np
from PIL import Image, ImageDraw

pyautogui.PAUSE = 0.1
EDGE_HWND = 0x1509c0

win32gui.ShowWindow(EDGE_HWND, win32con.SW_RESTORE)
win32gui.SetForegroundWindow(EDGE_HWND)
time.sleep(0.4)

# Click dropdown to open it
print("Opening dropdown...")
pyautogui.click(800, 928)
time.sleep(0.8)

img = pyautogui.screenshot()
arr = np.array(img)

# The dropdown list appeared at y=960-1025 (from chevron_click.png)
# Scan more carefully with 2px intervals
print("Scanning dropdown list area (y=955-1040):")
dark_rows = []
for sy in range(955, 1040):
    row = arr[sy, 530:1320, :]
    avg = row.mean()
    if avg < 248:
        dark_rows.append((sy, round(float(avg), 1)))

print(f"Dark rows: {dark_rows[:20]}")

# Save screenshot of the open dropdown
zoom = img.crop((520, 890, 1360, 1090))
draw = ImageDraw.Draw(zoom)
for x in range(0, zoom.width, 100):
    draw.line([(x,0),(x,zoom.height)], fill='red', width=1)
    draw.text((x+2,2), str(x+520), fill='red')
for y in range(0, zoom.height, 10):
    col = 'red' if y % 50 == 0 else 'pink'
    draw.line([(0,y),(zoom.width,y)], fill=col, width=1)
    draw.text((2,y+2), str(y+890), fill='blue')
zoom.save(r'C:\claude\personal-website\screenshots\open_dropdown_scan.png')
print("Saved open_dropdown_scan.png")

# Also raw image of the options area
raw = img.crop((520, 955, 1340, 1090))
raw.resize((raw.width, raw.height*4)).save(
    r'C:\claude\personal-website\screenshots\options_raw2.png')
print("Saved options_raw2.png")
