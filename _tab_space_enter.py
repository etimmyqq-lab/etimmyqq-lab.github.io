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

def snap(tag, y0=390, y1=660):
    img = pyautogui.screenshot()
    arr = np.array(img)
    r, g, b = arr[450, 700, :3]
    alive = r > 240 and g > 240 and b > 240
    crop = img.crop((215, y0, 1370, y1))
    draw = ImageDraw.Draw(crop)
    for x in range(0, crop.width, 100):
        draw.line([(x,0),(x,crop.height)], fill='red', width=1)
        draw.text((x+2,2), str(x+215), fill='red')
    for y in range(0, crop.height, 50):
        draw.line([(0,y),(crop.width,y)], fill='red', width=1)
        draw.text((2,y+2), str(y+y0), fill='red')
    crop.resize((crop.width//2, crop.height//2)).save(
        f'C:\\claude\\personal-website\\screenshots\\{tag}.png')
    return alive

# From dropdown_before_click.png: Tab+Space opens dropdown with
# "網頁應用程式" as the HIGHLIGHTED (focused) first item.
# Just pressing Enter should select it - no arrow keys needed.

print("Step 1: Click inside dialog right panel to focus...")
pyautogui.click(750, 600)
time.sleep(0.4)

print("Step 2: Tab to focus gear icon...")
pyautogui.press('tab')
time.sleep(0.4)

print("Step 3: Space to open type selector dropdown...")
pyautogui.press('space')
time.sleep(0.5)  # Short delay - dropdown is open with 網頁應用程式 highlighted

print("Step 4: Enter to select the highlighted item (網頁應用程式)...")
pyautogui.press('enter')
time.sleep(1.5)

alive = snap('tab_space_enter_result')
print(f"Dialog alive: {alive}")

if alive:
    # Check right panel for 網路應用程式 config
    img = pyautogui.screenshot()
    full = img.crop((215, 390, 1370, 800))
    draw = ImageDraw.Draw(full)
    for x in range(0, full.width, 100):
        draw.line([(x,0),(x,full.height)], fill='red', width=1)
        draw.text((x+2,2), str(x+215), fill='red')
    for y in range(0, full.height, 100):
        draw.line([(0,y),(full.width,y)], fill='red', width=1)
        draw.text((2,y+2), str(y+390), fill='red')
    full.resize((full.width//2, full.height//2)).save(
        r'C:\claude\personal-website\screenshots\webapp_result_final.png')
    print("Saved webapp_result_final.png - check right panel config")
else:
    print("Dialog closed!")
