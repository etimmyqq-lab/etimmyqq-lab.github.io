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

def snap(tag, y0=358, y1=1100, x1=1370):
    img = pyautogui.screenshot()
    crop = img.crop((215, y0, x1, y1))
    draw = ImageDraw.Draw(crop)
    for x in range(0, crop.width, 100):
        draw.line([(x,0),(x,crop.height)], fill='red', width=1)
        draw.text((x+2,2), str(x+215), fill='red')
    for y in range(0, crop.height, 100):
        draw.line([(0,y),(crop.width,y)], fill='red', width=1)
        draw.text((2,y+2), str(y+y0), fill='blue')
    crop.resize((crop.width//2, crop.height//2)).save(
        f'C:\\claude\\personal-website\\screenshots\\{tag}.png')
    arr = np.array(img)
    r, g, b = arr[450, 700, :3]
    return r > 240 and g > 240 and b > 240, img

# Step 1: Open deploy dialog
print("Step 1: Opening 部署 dropdown...")
pyautogui.click(1240, 375)
time.sleep(1.2)

print("Step 2: Click 新增部署作業...")
pyautogui.click(1210, 435)
time.sleep(2.5)

alive, img = snap('fresh1')
print(f"Dialog open: {alive}")

if not alive:
    print("ERROR: dialog not open")
    sys.exit(1)

# Step 3: Select 網頁應用程式
print("Step 3: Tab to gear, Space to open, Enter to select 網頁應用程式...")
pyautogui.click(800, 500)
time.sleep(0.3)
pyautogui.press('tab')
time.sleep(0.3)
pyautogui.press('space')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(1.5)

alive, img = snap('after_type_select')
arr = np.array(img)
right_brightness = arr[500:600, 530:1350, :].mean()
print(f"Right panel brightness after type select: {right_brightness:.1f} (should be <255 if config showing)")

if right_brightness > 253:
    print("WARNING: right panel still blank - type may not have been selected")
    # Try again with Tab+Space+Enter
    pyautogui.click(800, 500)
    time.sleep(0.3)
    pyautogui.press('tab')
    time.sleep(0.3)
    pyautogui.press('space')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(1.5)
    alive, img = snap('retry_type')

# Step 4: Set access to "所有已登入 Google 帳戶的使用者"
# The access dropdown is at y≈920-960. It defaults to "只有我自己" → press Down once
print("Step 4: Opening access dropdown and changing to all Google users...")
pyautogui.click(800, 928)
time.sleep(0.5)
pyautogui.press('down')
time.sleep(0.3)
alive, img = snap('after_access_set', 880, 1100)
arr = np.array(img)
print(f"Access field brightness (y=925-935): {arr[928, 530:1300, :].mean():.1f}")

# Step 5: Click 部署 button - located at bottom right of dialog
# From previous screenshots: 部署 at x≈1265-1355, y≈1035-1065
# Center: (1305, 1050)
print("Step 5: Clicking 部署 button at (1305, 1050)...")
pyautogui.click(1305, 1050)
time.sleep(4.0)  # Wait for deployment

# Step 6: Check for success - should show deployment URL dialog
alive, img = snap('deploy_success', 300, 900, 1400)
arr = np.array(img)
print(f"After deploy - pixel (700,450): {arr[450, 700, :3]}")
print("Check deploy_success.png for URL!")
