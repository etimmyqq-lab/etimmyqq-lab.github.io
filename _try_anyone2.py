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

def zoom_access(tag):
    img = pyautogui.screenshot()
    zoom = img.crop((520, 880, 1360, 1090))
    draw = ImageDraw.Draw(zoom)
    for x in range(0, zoom.width, 100):
        draw.line([(x,0),(x,zoom.height)], fill='red', width=1)
        draw.text((x+2,2), str(x+520), fill='red')
    for y in range(0, zoom.height, 20):
        col = 'red' if y % 100 == 0 else 'pink'
        draw.line([(0,y),(zoom.width,y)], fill=col, width=1)
        draw.text((2,y+2), str(y+880), fill='blue')
    zoom.resize((zoom.width//1, zoom.height//1)).save(
        f'C:\\claude\\personal-website\\screenshots\\{tag}.png')
    return img

# Dropdown field is at y≈970-1020 from access_zoom.png
# Click the dropdown area to focus it
print("Clicking dropdown field at (930, 995)...")
pyautogui.click(930, 995)
time.sleep(0.5)
zoom_access('focused_drop')

# Try pressing Down
print("Pressing Down...")
pyautogui.press('down')
time.sleep(0.5)
zoom_access('down4_result')

# Read what's showing
img = pyautogui.screenshot()
zoom = img.crop((520, 880, 1360, 1090))
zoom.save(r'C:\claude\personal-website\screenshots\access_current.png')

arr = np.array(img)
# Scan y=920-970 for text brightness (the "selected value" area)
print("\nText area scan y=920-945:")
for sy in range(920, 950):
    row = arr[sy, 530:1320, :]
    avg = row.mean()
    if avg < 240:
        print(f"  y={sy}: brightness={avg:.1f}")

# Try clicking the down-arrow chevron at far right of dropdown
# From access_zoom: ▼ is at approximately x=1290-1310, y=930
print("\nTrying to click chevron ▼ at (1305, 930)...")
pyautogui.click(1305, 930)
time.sleep(0.8)
zoom_access('chevron_click')

# Check for dropdown list appearing below the dropdown field (y>1020)
img2 = pyautogui.screenshot()
arr2 = np.array(img2)
print("Scanning for dropdown list below field (y=1020-1300):")
for sy in range(1020, 1300, 10):
    row = arr2[sy, 530:1340, :]
    avg = row.mean()
    if avg < 240:
        print(f"  y={sy}: brightness={avg:.1f}")
