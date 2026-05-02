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
    crop = img.crop((215, 358, 1370, 850))
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

# Dropdown is visible. "網頁應用程式" is the first option.
# From after_space.png: dropdown items in left panel around x=350-530 screen, y≈460-480
# Try clicking "網頁應用程式" at estimated positions
print("Current state:")
snap('before_webapp_click')

# From half-size image analysis:
# crop starts at (215, 358), half-size
# "網頁應用程式" appears at image coords ~(175, 72) half-size
# => screen x = 175*2+215 = 565, screen y = 72*2+358 = 502
# But let me try a few positions to be safe

for y_try in [465, 478, 490]:
    for x_try in [400, 450, 510]:
        print(f"Trying click at ({x_try}, {y_try})...")
        pyautogui.click(x_try, y_try)
        time.sleep(1.0)
        img = pyautogui.screenshot()
        arr = np.array(img)
        r, g, b = arr[450, 700, :3]
        alive = r > 240 and g > 240 and b > 240
        snap(f'webapp_try_{x_try}_{y_try}')
        print(f"  Dialog alive: {alive}")

        # Check if type was selected - look for "網路應用程式" text in settings panel
        # If we selected it, the right panel should show configuration options
        # Take a wider screenshot to check
        full = img.crop((215, 358, 1370, 900))
        full.resize((full.width//2, full.height//2)).save(
            f'C:\\claude\\personal-website\\screenshots\\webapp_full_{x_try}_{y_try}.png')

        if alive:
            print(f"  -> Check webapp_full_{x_try}_{y_try}.png for configuration panel")
            break
    if alive:
        break

print("Done - check screenshots to see if web app type was selected")
