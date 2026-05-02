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
    crop = img.crop((215, 880, 1370, 1250))
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

# The "只有我自己" dropdown is at y≈910-945, focused with up-arrow visible
# Click the dropdown chevron (▲ at right end) to open options
# The dropdown at approximately screen x=540-1340, y≈920
# Chevron at far right ~x=1330, y≈930

print("Clicking dropdown chevron to open options...")
pyautogui.click(930, 930)
time.sleep(0.8)
snap_bottom('after_access_click')

# Try pressing Down arrow to navigate options
print("Pressing Down to show options or navigate to '所有人'...")
pyautogui.press('down')
time.sleep(0.5)
snap_bottom('after_down1')

# Check what's visible now - should see "所有人" or list
img = pyautogui.screenshot()
arr = np.array(img)
print("Scanning for dropdown content (y=950-1100):")
for sy in range(950, 1100, 10):
    row = arr[sy, 530:1340, :]
    avg = row.mean()
    if avg < 240:
        print(f"  y={sy}: brightness={avg:.1f}")

snap_bottom('access_options')

# If "所有人" is an option visible, it should appear in the dropdown list
# Try pressing Down again
print("Pressing Down again...")
pyautogui.press('down')
time.sleep(0.5)
snap_bottom('after_down2')

# Press Enter to confirm selection
print("Pressing Enter to confirm selection...")
pyautogui.press('enter')
time.sleep(0.8)
snap_bottom('access_set')

# Full screenshot showing both panels
img = pyautogui.screenshot()
full = img.crop((215, 358, 1370, 1100))
draw = ImageDraw.Draw(full)
for x in range(0, full.width, 100):
    draw.line([(x,0),(x,full.height)], fill='red', width=1)
    draw.text((x+2,2), str(x+215), fill='red')
for y in range(0, full.height, 100):
    draw.line([(0,y),(full.width,y)], fill='red', width=1)
    draw.text((2,y+2), str(y+358), fill='blue')
full.resize((full.width//2, full.height//2)).save(
    r'C:\claude\personal-website\screenshots\full_after_access.png')
print("Saved full_after_access.png")
