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

def is_dialog_open():
    img = pyautogui.screenshot()
    arr = np.array(img)
    r, g, b = arr[450, 700, :3]
    return r > 240 and g > 240 and b > 240, img

def snap_full(img, tag):
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

# Step 1: Open deploy dropdown
print("Opening deploy dropdown...")
pyautogui.click(1240, 375)
time.sleep(1.2)
alive, img = is_dialog_open()
snap_full(img, 'step1_dropdown')
print(f"After 部署▼ click: {alive}")

# Step 2: Click 新增部署作業
print("Clicking 新增部署作業 at (1210, 435)...")
pyautogui.click(1210, 435)
time.sleep(2.0)
alive, img = is_dialog_open()
snap_full(img, 'step2_dialog')
print(f"Dialog open: {alive}")

if not alive:
    print("ERROR: Dialog did not open")
    sys.exit(1)

# Step 3: Click right panel to set focus (avoid left nav and gear row)
print("Focusing dialog at (750, 600)...")
pyautogui.click(750, 600)
time.sleep(0.5)

# Step 4: Tab to gear + Space to open dropdown
print("Tab + Space to open type selector...")
pyautogui.press('tab')
time.sleep(0.5)
_, img = is_dialog_open()
snap_full(img, 'step4_tab')

pyautogui.press('space')
time.sleep(1.0)
alive, img = is_dialog_open()
snap_full(img, 'step5_dropdown_open')
print(f"Type dropdown open: {alive}")

if not alive:
    print("ERROR: Dropdown closed dialog")
    sys.exit(1)

# Step 5: Take zoomed screenshot of the dropdown area to calibrate
# Dropdown should be in left panel y≈420-550
zoom_drop = img.crop((215, 400, 520, 560))
zoom_drop.resize((zoom_drop.width*3, zoom_drop.height*3)).save(
    r'C:\claude\personal-website\screenshots\dropdown_zoom.png')
print("Saved dropdown_zoom.png - examine for precise click coords")

# Also save annotated version with pixel coords
ann = img.crop((215, 400, 520, 560))
draw2 = ImageDraw.Draw(ann)
for x in range(0, ann.width, 20):
    draw2.line([(x,0),(x,ann.height)], fill='blue', width=1)
    draw2.text((x+1,1), str(x+215), fill='blue')
for y in range(0, ann.height, 20):
    draw2.line([(0,y),(ann.width,y)], fill='blue', width=1)
    draw2.text((1,y+1), str(y+400), fill='blue')
ann.resize((ann.width*3, ann.height*3)).save(
    r'C:\claude\personal-website\screenshots\dropdown_annotated.png')
print("Saved dropdown_annotated.png")

print("\nNow attempting to click '網頁應用程式'...")
print("Based on after_space.png, trying y≈468-485...")

# Try clicking Down arrow to navigate to first item, then Enter
# This is safer than trying to click exact pixel
pyautogui.press('down')
time.sleep(0.4)
alive, img = is_dialog_open()
snap_full(img, 'step6_down_arrow')
print(f"After Down arrow: {alive}")

if alive:
    pyautogui.press('enter')
    time.sleep(1.0)
    alive, img = is_dialog_open()
    snap_full(img, 'step7_after_enter')
    print(f"After Enter select: {alive}")

    if alive:
        print("SUCCESS - type selected! Checking right panel for config...")
        # Save full dialog showing config panel
        full = img.crop((215, 358, 1370, 1000))
        draw = ImageDraw.Draw(full)
        for x in range(0, full.width, 100):
            draw.line([(x,0),(x,full.height)], fill='red', width=1)
            draw.text((x+2,2), str(x+215), fill='red')
        for y in range(0, full.height, 100):
            draw.line([(0,y),(full.width,y)], fill='red', width=1)
            draw.text((2,y+2), str(y+358), fill='red')
        full.resize((full.width//2, full.height//2)).save(
            r'C:\claude\personal-website\screenshots\config_panel_full.png')
        print("Saved config_panel_full.png")
    else:
        print("Enter closed dialog after Down")
