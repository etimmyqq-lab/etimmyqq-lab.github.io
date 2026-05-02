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

def snap(tag, y0=390, y1=750, full_width=True):
    img = pyautogui.screenshot()
    x1 = 1370 if full_width else 530
    crop = img.crop((215, y0, x1, y1))
    draw = ImageDraw.Draw(crop)
    for x in range(0, crop.width, 100 if full_width else 20):
        draw.line([(x,0),(x,crop.height)], fill='red', width=1)
        draw.text((x+2,2), str(x+215), fill='red')
    for y in range(0, crop.height, 50 if full_width else 10):
        col = 'red' if y % 100 == 0 else 'pink'
        draw.line([(0,y),(crop.width,y)], fill=col, width=1)
        draw.text((2,y+2), str(y+y0), fill='blue')
    scale = 1 if full_width else 3
    crop.resize((crop.width//(2 if full_width else 1)*scale,
                 crop.height//(2 if full_width else 1)*scale)).save(
        f'C:\\claude\\personal-website\\screenshots\\{tag}.png')
    arr = np.array(img)
    r, g, b = arr[450, 700, :3]
    return r > 240 and g > 240 and b > 240, img

# Step 1: Press Escape to dismiss current dialog
print("Pressing Escape to dismiss current dialog...")
pyautogui.press('escape')
time.sleep(1.0)

# Step 2: Re-open 部署 dropdown
print("Opening 部署 dropdown...")
pyautogui.click(1240, 375)
time.sleep(1.2)

# Step 3: Click 新增部署作業
print("Clicking 新增部署作業...")
pyautogui.click(1210, 435)
time.sleep(2.5)

alive, img = snap('fresh_dialog')
arr = np.array(img)
print(f"Fresh dialog open: {alive}")

if alive:
    # The fresh dialog should have NO type selected in left panel
    # Right panel should be blank (no config text)
    # Check right panel content
    right = arr[450:600, 520:1360, :]
    print(f"Right panel avg brightness (blank if ~255): {right.mean():.1f}")

    # Step 4: Click inside the BLANK right panel to set focus
    print("Clicking blank right panel to focus...")
    pyautogui.click(800, 500)
    time.sleep(0.3)

    # Step 5: Tab to focus gear
    print("Tab to focus gear...")
    pyautogui.press('tab')
    time.sleep(0.4)
    snap('after_tab_fresh', 390, 650)

    # Step 6: Space to open dropdown
    print("Space to open dropdown...")
    pyautogui.press('space')
    time.sleep(0.5)

    # Capture immediately
    alive2, img2 = snap('dropdown_fresh_open', 460, 650, full_width=False)
    arr2 = np.array(img2)

    # Look for dropdown content below gear (y=487-540), SENSITIVE threshold
    found = []
    for sy in range(487, 545):
        row = arr2[sy, 225:510, :]
        avg = row.mean()
        if avg < 250:
            found.append((sy, round(float(avg), 1)))
    print(f"New content after Space (y=487-545): {found}")

    if found:
        print(f"\nDropdown detected! Pressing Enter to select first item...")
        pyautogui.press('enter')
        time.sleep(1.5)
        alive3, img3 = snap('after_enter_fresh')
        print(f"Dialog alive after Enter: {alive3}")
    else:
        print("No dropdown detected via pixel scan - taking full screenshot for inspection")
        snap('after_space_full', 360, 850)
