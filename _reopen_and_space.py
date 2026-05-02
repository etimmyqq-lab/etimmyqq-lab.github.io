# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import win32gui, win32con, win32clipboard
import time
import pyautogui
import numpy as np
from PIL import Image, ImageDraw

pyautogui.PAUSE = 0.3
EDGE_HWND = 0x1509c0

win32gui.ShowWindow(EDGE_HWND, win32con.SW_RESTORE)
win32gui.SetForegroundWindow(EDGE_HWND)
time.sleep(0.4)

def snap(tag):
    img = pyautogui.screenshot()
    arr = np.array(img)
    # Check if dialog is open: look for white area in dialog zone
    r, g, b = arr[450, 700, :3]
    alive = r > 240 and g > 240 and b > 240
    crop = img.crop((215, 358, 1370, 700))
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

# Step 1: click 部署▼ button to open dropdown
print("Clicking 部署▼ at (1240, 375)...")
pyautogui.click(1240, 375)
time.sleep(1.2)
alive = snap('deploy_dropdown')
print(f"After deploy click, white at (700,450): {alive}")

# Step 2: click 新增部署作業 in dropdown
print("Clicking 新增部署作業 at (1210, 435)...")
pyautogui.click(1210, 435)
time.sleep(2.0)
alive = snap('new_deploy_dialog')
print(f"Dialog opened: {alive}")

if not alive:
    print("Dialog did not open. Trying again...")
    pyautogui.click(1240, 375)
    time.sleep(1.2)
    pyautogui.click(1210, 435)
    time.sleep(2.0)
    alive = snap('new_deploy_retry')
    print(f"Retry dialog open: {alive}")

if alive:
    # Step 3: click right panel to focus dialog (avoid left nav panel)
    print("Clicking (750, 550) to focus dialog right panel...")
    pyautogui.click(750, 550)
    time.sleep(0.5)

    # Step 4: Tab once to focus gear
    print("Tab to focus gear...")
    pyautogui.press('tab')
    time.sleep(0.6)
    snap('tab1_gear')

    # Step 5: Try Space to activate gear (not Enter)
    print("Pressing Space to activate gear...")
    pyautogui.press('space')
    time.sleep(1.5)
    alive = snap('after_space')
    print(f"Dialog alive after Space: {alive}")

    if alive:
        print("SUCCESS - type selector should be showing!")
    else:
        print("Space also closed dialog. Will try direct click approach.")
