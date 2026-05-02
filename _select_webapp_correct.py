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

def snap(tag):
    img = pyautogui.screenshot()
    arr = np.array(img)
    r, g, b = arr[450, 700, :3]
    alive = r > 240 and g > 240 and b > 240
    crop = img.crop((215, 358, 1370, 950))
    draw = ImageDraw.Draw(crop)
    for x in range(0, crop.width, 100):
        draw.line([(x,0),(x,crop.height)], fill='red', width=1)
        draw.text((x+2,2), str(x+215), fill='red')
    for y in range(0, crop.height, 50):
        draw.line([(0,y),(crop.width,y)], fill='red', width=1)
        draw.text((2,y+2), str(y+358), fill='red')
    crop.resize((crop.width//2, crop.height//2)).save(
        f'C:\\claude\\personal-website\\screenshots\\{tag}.png')
    return alive, img

# Dialog is open with "API 執行檔" selected.
# Need to go back to gear icon and open dropdown, then press Up (not Down) to get to 網頁應用程式
# OR: Tab + Space reopens dropdown, then press Up once to reach 網頁應用程式

print("Current state - clicking right panel to focus...")
pyautogui.click(750, 600)
time.sleep(0.4)

# Tab to gear icon
print("Tab to gear icon...")
pyautogui.press('tab')
time.sleep(0.5)

# Space to open dropdown
print("Space to open dropdown...")
pyautogui.press('space')
time.sleep(1.0)
alive, img = snap('reopen_dropdown')
print(f"Dropdown open: {alive}")

if alive:
    # "網頁應用程式" is the first item - press Up to go to it from "API 執行檔" focus
    # Or press Home to go to first item
    # Actually: when dropdown opens, the current selection (API 執行檔) is highlighted
    # Press Up once to move to 網頁應用程式 (the item above API 執行檔)
    print("Pressing Up to move to 網頁應用程式...")
    pyautogui.press('up')
    time.sleep(0.4)
    snap('after_up')

    print("Pressing Enter to confirm selection...")
    pyautogui.press('enter')
    time.sleep(1.2)
    alive, img = snap('webapp_type_selected')
    print(f"Dialog alive after Enter: {alive}")

    if alive:
        print("SUCCESS! Checking config panel...")
        full = img.crop((215, 358, 1370, 1050))
        draw = ImageDraw.Draw(full)
        for x in range(0, full.width, 100):
            draw.line([(x,0),(x,full.height)], fill='red', width=1)
            draw.text((x+2,2), str(x+215), fill='red')
        for y in range(0, full.height, 100):
            draw.line([(0,y),(full.width,y)], fill='red', width=1)
            draw.text((2,y+2), str(y+358), fill='red')
        full.resize((full.width//2, full.height//2)).save(
            r'C:\claude\personal-website\screenshots\webapp_config_final.png')
        print("Saved webapp_config_final.png")
    else:
        print("ERROR: dialog closed")
