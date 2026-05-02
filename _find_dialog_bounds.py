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

# Re-open the deployment dialog
win32gui.ShowWindow(EDGE_HWND, win32con.SW_RESTORE)
win32gui.SetForegroundWindow(EDGE_HWND)
time.sleep(0.4)

# Open 部署 dropdown
pyautogui.click(1240, 375)
time.sleep(1.2)
# Click 新增部署作業
pyautogui.click(1210, 435)
time.sleep(2.5)

img = pyautogui.screenshot()
arr = np.array(img)

# Find rows/columns where pixel is nearly pure white (dialog background)
# White = R>240, G>240, B>240
white_mask = (arr[:,:,0] > 240) & (arr[:,:,1] > 240) & (arr[:,:,2] > 240)

# Scan y=200 to y=1200, x=100 to x=1500 to find dialog
# Find the bounding box of the largest white region
rows = np.any(white_mask[200:1200, 100:1500], axis=1)
cols = np.any(white_mask[200:1200, 100:1500], axis=0)

y_indices = np.where(rows)[0] + 200
x_indices = np.where(cols)[0] + 100

if len(y_indices) > 0 and len(x_indices) > 0:
    print(f"White region y: {y_indices[0]} to {y_indices[-1]}")
    print(f"White region x: {x_indices[0]} to {x_indices[-1]}")

    # Save annotated image
    dialog_crop = img.crop((x_indices[0]-10, y_indices[0]-10,
                             x_indices[-1]+10, y_indices[-1]+10))
    draw = ImageDraw.Draw(dialog_crop)
    # Mark the "選取類型" area — top-left quadrant
    draw.rectangle([(0,0),(dialog_crop.width//3, 60)], outline='blue', width=3)
    dialog_crop.resize((dialog_crop.width//2, dialog_crop.height//2)).save(
        r'C:\claude\personal-website\screenshots\dialog_bounds.png')
    print(f"Dialog size: {dialog_crop.size}")
else:
    print("No white region found — dialog may be closed")
    img.resize((1280, 720)).save(r'C:\claude\personal-website\screenshots\dialog_bounds.png')
