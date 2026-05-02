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
    r, g, b = np.array(img)[600, 700, :3]
    alive = r > 240 and g > 240 and b > 240
    crop = img.crop((215, 358, 1370, 800))
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

# Step 1: take initial screenshot to see current state
alive = snap('before_gear')
print(f"Dialog open before: {alive}")

if not alive:
    print("Dialog not open! Need to reopen it.")
else:
    # Step 2: click inside right panel to focus dialog
    print("Clicking (700, 600) to focus dialog...")
    pyautogui.click(700, 600)
    time.sleep(0.5)

    # Step 3: press Tab once to focus the gear icon
    print("Pressing Tab to focus gear icon...")
    pyautogui.press('tab')
    time.sleep(0.6)
    snap('after_tab1')

    # Step 4: press Enter to activate gear
    print("Pressing Enter to activate gear...")
    pyautogui.press('enter')
    time.sleep(1.0)
    alive = snap('after_enter')
    print(f"Dialog open after Enter: {alive}")

    if alive:
        print("Type selector should now be visible!")
    else:
        print("Dialog closed - Enter may have triggered wrong button")
