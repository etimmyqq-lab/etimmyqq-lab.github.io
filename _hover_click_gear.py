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

def check_dropdown(tag=None):
    """Return True if dropdown items appeared (new dark content below gear row)"""
    img = pyautogui.screenshot()
    arr = np.array(img)
    # Check for NEW content between y=490-540 (below gear at 472, above API 執行檔 at 540)
    new_content = False
    for sy in range(490, 538):
        row = arr[sy, 230:500, :]
        if row.mean() < 235:
            new_content = True
            break

    dialog_open = arr[450, 700, :3].mean() > 240

    if tag:
        crop = img.crop((215, 390, 520, 650))
        draw = ImageDraw.Draw(crop)
        for x in range(0, crop.width, 20):
            draw.line([(x,0),(x,crop.height)], fill='red', width=1)
            draw.text((x+1,1), str(x+215), fill='red')
        for y in range(0, crop.height, 20):
            draw.line([(0,y),(crop.width,y)], fill='blue', width=1)
            draw.text((1,y+1), str(y+390), fill='blue')
        crop.resize((crop.width*3, crop.height*3)).save(
            f'C:\\claude\\personal-website\\screenshots\\{tag}.png')
    return dialog_open, new_content, img

# Gear center at approximately (488, 473)
# Try hover then click
for gx, gy in [(488, 473), (486, 472), (490, 474), (485, 470), (492, 476), (480, 472)]:
    print(f"\nTrying hover+click at ({gx}, {gy})...")
    pyautogui.moveTo(gx, gy, duration=0.3)
    time.sleep(0.5)  # hover to activate
    pyautogui.click(gx, gy)
    time.sleep(1.0)
    dialog_open, new_content, img = check_dropdown(f'hover_{gx}_{gy}')
    print(f"  dialog={dialog_open}, dropdown_appeared={new_content}")

    if new_content:
        print(f"  SUCCESS! Dropdown appeared at ({gx}, {gy})")
        break
    if not dialog_open:
        print(f"  Dialog closed - click landed outside")
        break

# If still no dropdown, try double-click
if dialog_open and not new_content:
    print("\nTrying double-click on gear (488, 473)...")
    pyautogui.doubleClick(488, 473)
    time.sleep(1.0)
    dialog_open, new_content, img = check_dropdown('double_click')
    print(f"  dialog={dialog_open}, dropdown_appeared={new_content}")
