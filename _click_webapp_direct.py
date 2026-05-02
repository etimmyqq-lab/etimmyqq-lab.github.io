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

# From after_up.png analysis: dropdown items visible
# Crop (215,358)→(1370,950), half-size
# "網頁應用程式" (1st item) at half-image y≈55-65
# → screen y = 55*2+358=468 to 65*2+358=488  → target y≈472
# item x center at half-image x≈160 → screen x = 160*2+215=535
# But left panel is x=215-514, so dropdown items x≈250-510 screen
# → target x≈380

# Re-open dropdown via Tab+Space
print("Focusing dialog...")
pyautogui.click(750, 600)
time.sleep(0.4)
print("Tab to gear...")
pyautogui.press('tab')
time.sleep(0.5)
print("Space to open dropdown...")
pyautogui.press('space')
time.sleep(1.0)

alive, img = snap('dropdown_before_click')
print(f"Dropdown open: {alive}")

# Zoom into dropdown area to verify
drop_zoom = img.crop((215, 420, 520, 570))
draw = ImageDraw.Draw(drop_zoom)
for x in range(0, drop_zoom.width, 20):
    draw.line([(x,0),(x,drop_zoom.height)], fill='blue', width=1)
    draw.text((x+1,0), str(x+215), fill='blue')
for y in range(0, drop_zoom.height, 20):
    draw.line([(0,y),(drop_zoom.width,y)], fill='blue', width=1)
    draw.text((0,y+1), str(y+420), fill='blue')
drop_zoom.resize((drop_zoom.width*3, drop_zoom.height*3)).save(
    r'C:\claude\personal-website\screenshots\dropdown_zoom2.png')
print("Saved dropdown_zoom2.png")

if alive:
    # Click directly on "網頁應用程式" text
    # From after_up.png: item appears at screen (380, 465)
    # The dropdown floats over the left panel
    # Items: 網頁應用程式 ≈ y=465, API執行檔 ≈ y=490, 外掛程式 ≈ y=515, 資料庫 ≈ y=540
    target_x = 380
    target_y = 465

    print(f"Clicking '網頁應用程式' at ({target_x}, {target_y})...")
    pyautogui.click(target_x, target_y)
    time.sleep(1.5)

    alive, img = snap('after_webapp_click')
    print(f"Dialog alive: {alive}")

    if alive:
        # Check left panel for selected type
        full = img.crop((215, 358, 1370, 1050))
        draw = ImageDraw.Draw(full)
        for x in range(0, full.width, 100):
            draw.line([(x,0),(x,full.height)], fill='red', width=1)
            draw.text((x+2,2), str(x+215), fill='red')
        for y in range(0, full.height, 100):
            draw.line([(0,y),(full.width,y)], fill='red', width=1)
            draw.text((2,y+2), str(y+358), fill='red')
        full.resize((full.width//2, full.height//2)).save(
            r'C:\claude\personal-website\screenshots\webapp_selected_final.png')
        print("Saved webapp_selected_final.png - check right panel for 網路應用程式 config")
    else:
        print("Dialog closed - may have hit outside. Check screenshots.")
