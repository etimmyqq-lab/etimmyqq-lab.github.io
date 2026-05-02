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

def snap(tag, x0=0, y0=300, x1=1400, y1=900):
    img = pyautogui.screenshot()
    crop = img.crop((x0, y0, x1, y1))
    draw = ImageDraw.Draw(crop)
    for x in range(0, crop.width, 100):
        draw.line([(x,0),(x,crop.height)], fill='red', width=1)
        draw.text((x+2,2), str(x+x0), fill='red')
    for y in range(0, crop.height, 50):
        draw.line([(0,y),(crop.width,y)], fill='red', width=1)
        draw.text((2,y+2), str(y+y0), fill='blue')
    crop.resize((crop.width//2, crop.height//2)).save(
        f'C:\\claude\\personal-website\\screenshots\\{tag}.png')
    return img

# Take snapshot to see current state
img = snap('grant_current')

# Scan for the blue "授予存取權" button
arr = np.array(img)
print("Scanning for blue button (authorization button)...")
# Blue button: B > R and B > G significantly, or a specific blue color
for sy in range(350, 550, 5):
    row = arr[sy, 215:700, :]
    # Blue pixels: B > 150, B > R+50
    blue_mask = (row[:, 2].astype(int) - row[:, 0].astype(int)) > 80
    blue_count = blue_mask.sum()
    if blue_count > 20:
        blue_xs = np.where(blue_mask)[0] + 215
        print(f"  y={sy}: {blue_count} blue pixels at x={blue_xs[:3].tolist()}...{blue_xs[-3:].tolist()}")

# The button should be at approximately screen y≈400-430, x≈235-450
# Click it
print("\nClicking '授予存取權' button...")
pyautogui.click(340, 415)
time.sleep(3.0)

snap('after_grant', 0, 300, 1400, 1000)
print("Saved after_grant.png")

# Check if a Google auth window opened
img2 = pyautogui.screenshot()
full = img2.crop((0, 0, 1400, 900))
full.resize((700, 450)).save(r'C:\claude\personal-website\screenshots\after_grant_full.png')
print("Saved after_grant_full.png")
