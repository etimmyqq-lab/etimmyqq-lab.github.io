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
    crop = img.crop((215, 358, 1370, 900))
    draw = ImageDraw.Draw(crop)
    for x in range(0, crop.width, 100):
        draw.line([(x,0),(x,crop.height)], fill='red', width=1)
        draw.text((x+2,2), str(x+215), fill='red')
    for y in range(0, crop.height, 50):
        draw.line([(0,y),(crop.width,y)], fill='red', width=1)
        draw.text((2,y+2), str(y+358), fill='red')
    crop.resize((crop.width//2, crop.height//2)).save(
        f'C:\\claude\\personal-website\\screenshots\\{tag}.png')
    return alive

# The dropdown is visible with "網頁應用程式" as first option.
# From after_space.png: items at screen y≈465-495, x≈350-500
# "網頁應用程式" (first item) at approximately screen (430, 468)

print("Clicking '網頁應用程式' at (430, 468)...")
pyautogui.click(430, 468)
time.sleep(1.5)
alive = snap('webapp_selected')
print(f"Dialog alive: {alive}")

if alive:
    # Take a full screenshot to see configuration panel
    img = pyautogui.screenshot()
    full = img.crop((215, 358, 1370, 1000))
    draw = ImageDraw.Draw(full)
    for x in range(0, full.width, 100):
        draw.line([(x,0),(x,full.height)], fill='red', width=1)
        draw.text((x+2,2), str(x+215), fill='red')
    for y in range(0, full.height, 100):
        draw.line([(0,y),(full.width,y)], fill='red', width=1)
        draw.text((2,y+2), str(y+358), fill='red')
    full.resize((full.width//2, full.height//2)).save(
        r'C:\claude\personal-website\screenshots\webapp_config_panel.png')
    print("Saved webapp_config_panel.png - check if '網路應用程式' config is shown")
else:
    print("Dialog closed - need to retry")
