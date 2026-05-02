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

def snap_full(tag, y0=880, y1=1300):
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

# Click the dropdown chevron ▼ at right end of "誰可以存取" dropdown
# Dropdown spans x≈540-1340, y≈970-1000
# Chevron (▼) is at far right: x≈1320-1340, y≈985
print("Clicking chevron ▼ of 誰可以存取 dropdown...")
pyautogui.click(1325, 985)
time.sleep(1.0)

snap_full('access_list_open')

img = pyautogui.screenshot()
# Scan for dropdown list content (should appear below or at the dropdown)
arr = np.array(img)
print("Scanning for dropdown list (y=1000-1300):")
for sy in range(1000, 1300, 10):
    row = arr[sy, 530:1340, :]
    avg = row.mean()
    if avg < 245:
        print(f"  y={sy}: brightness={avg:.1f}")

snap_full('access_list_full', 880, 1400)
print("Saved access_list_full.png")
