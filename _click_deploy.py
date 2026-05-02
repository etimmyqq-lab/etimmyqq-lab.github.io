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
time.sleep(0.4)

def snap(tag, y0=880, y1=1150):
    img = pyautogui.screenshot()
    crop = img.crop((215, y0, 1370, y1))
    draw = ImageDraw.Draw(crop)
    for x in range(0, crop.width, 100):
        draw.line([(x,0),(x,crop.height)], fill='red', width=1)
        draw.text((x+2,2), str(x+215), fill='red')
    for y in range(0, crop.height, 50):
        draw.line([(0,y),(crop.width,y)], fill='red', width=1)
        draw.text((2,y+2), str(y+y0), fill='blue')
    crop.resize((crop.width//2, crop.height//2)).save(
        f'C:\\claude\\personal-website\\screenshots\\{tag}.png')
    return img

# First make sure we're in correct state - close any open dropdown
print("Pressing Escape to close any open dropdown...")
pyautogui.press('escape')
time.sleep(0.5)

# Take snapshot to confirm state
snap('before_deploy')

# Click 部署 button - from access_zoom.png:
# Button at x=1265-1360, y=1035-1065 → center (1310, 1050)
print("Clicking 部署 button at (1310, 1050)...")
pyautogui.click(1310, 1050)
time.sleep(3.0)  # Wait for deployment to process

# Take screenshot - should show success dialog with deployment URL
img = pyautogui.screenshot()
full = img.crop((0, 300, 1400, 1000))
draw = ImageDraw.Draw(full)
for x in range(0, full.width, 100):
    draw.line([(x,0),(x,full.height)], fill='red', width=1)
    draw.text((x+2,2), str(x), fill='red')
for y in range(0, full.height, 50):
    draw.line([(0,y),(full.width,y)], fill='red', width=1)
    draw.text((2,y+2), str(y+300), fill='blue')
full.resize((full.width//2, full.height//2)).save(
    r'C:\claude\personal-website\screenshots\deploy_result.png')
print("Saved deploy_result.png")

# Check if deployment URL is visible
arr = np.array(img)
r, g, b = arr[450, 700, :3]
print(f"Pixel check (700,450): rgb=({r},{g},{b})")
