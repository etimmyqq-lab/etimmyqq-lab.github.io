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

def snap_bottom(tag):
    img = pyautogui.screenshot()
    crop = img.crop((215, 880, 1370, 1150))
    draw = ImageDraw.Draw(crop)
    for x in range(0, crop.width, 100):
        draw.line([(x,0),(x,crop.height)], fill='red', width=1)
        draw.text((x+2,2), str(x+215), fill='red')
    for y in range(0, crop.height, 50):
        draw.line([(0,y),(crop.width,y)], fill='red', width=1)
        draw.text((2,y+2), str(y+880), fill='blue')
    crop.resize((crop.width//2, crop.height//2)).save(
        f'C:\\claude\\personal-website\\screenshots\\{tag}.png')
    return img

# Current: "所有已登入 Google 帳戶的使用者" is selected
# Need: "所有人" (Anyone) - press Down to get the next option

print("Clicking dropdown to refocus...")
pyautogui.click(930, 985)  # click the dropdown field
time.sleep(0.5)
snap_bottom('before_down3')

print("Pressing Down to get next option (所有人)...")
pyautogui.press('down')
time.sleep(0.5)
snap_bottom('after_down3')

# Check what we have now
img = pyautogui.screenshot()
# Check the dropdown text area
crop_text = img.crop((540, 970, 1320, 1010))
crop_text.resize((crop_text.width*2, crop_text.height*2)).save(
    r'C:\claude\personal-website\screenshots\access_text_zoom.png')
print("Saved access_text_zoom.png")
