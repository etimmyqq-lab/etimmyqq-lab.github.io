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

def full_snap(tag, y_start=358, y_end=650):
    img = pyautogui.screenshot()
    crop = img.crop((215, y_start, 1370, y_end))
    draw = ImageDraw.Draw(crop)
    for x in range(0, crop.width, 50):
        draw.line([(x,0),(x,crop.height)], fill='red', width=1)
        draw.text((x+1,1), str(x+215), fill='red')
    for y in range(0, crop.height, 20):
        col = 'red' if y % 100 == 0 else 'pink'
        draw.line([(0,y),(crop.width,y)], fill=col, width=1)
        draw.text((1,y+1), str(y+y_start), fill='red')
    crop.resize((crop.width//2, crop.height//2)).save(
        f'C:\\claude\\personal-website\\screenshots\\{tag}.png')
    return img

# Step 1: Snapshot the current dialog state
print("Initial state snapshot...")
full_snap('gear_initial', 358, 700)

# Step 2: Open the dropdown using 部署▼ → 新增部署作業 freshly
# First check if dialog is already open
img = pyautogui.screenshot()
arr = np.array(img)
r, g, b = arr[450, 700, :3]
dialog_open = r > 240 and g > 240 and b > 240
print(f"Dialog open: {dialog_open}")

if not dialog_open:
    print("Re-opening dialog...")
    pyautogui.click(1240, 375)
    time.sleep(1.2)
    pyautogui.click(1210, 435)
    time.sleep(2.0)
    img = pyautogui.screenshot()
    arr = np.array(img)
    r, g, b = arr[450, 700, :3]
    dialog_open = r > 240 and g > 240 and b > 240
    print(f"Dialog after reopen: {dialog_open}")

# Step 3: Take fine-grained snapshot to find gear position
full_snap('gear_dialog', 358, 600)

# Step 4: Scan for the gear row by looking for the non-white area
# The "選取類型" row + gear is somewhere in the dialog
print("\nScanning for non-white rows in left panel (x=215-514)...")
img = pyautogui.screenshot()
arr = np.array(img)
prev_bright = True
for sy in range(358, 600):
    row_pixels = arr[sy, 220:510, :]
    avg_brightness = row_pixels.mean()
    if avg_brightness < 240 and prev_bright:
        print(f"  Dark band starts at y={sy} (brightness={avg_brightness:.1f})")
        prev_bright = False
    elif avg_brightness >= 240 and not prev_bright:
        print(f"  Light band starts at y={sy}")
        prev_bright = True

# Step 5: Click the gear - from dropdown_precise.png, gear is at ~(471, 473)
# Also try the gear at slightly different y positions
print("\nAttempting gear click at (471, 473)...")
pyautogui.click(471, 473)
time.sleep(1.0)

img = pyautogui.screenshot()
arr = np.array(img)
r, g, b = arr[450, 700, :3]
alive = r > 240 and g > 240 and b > 240
print(f"Dialog alive after gear click: {alive}")

full_snap('after_gear473', 380, 620)

if alive:
    print("Scanning for dropdown items in left panel...")
    for sy in range(450, 620):
        row_pixels = arr[sy, 220:510, :]
        avg_b = row_pixels.mean()
        if avg_b < 240:
            print(f"  Non-white at y={sy}: brightness={avg_b:.1f}")

    print("\nTaking zoomed dropdown area shot (y=450-620)...")
    zoom = img.crop((215, 450, 520, 620))
    draw = ImageDraw.Draw(zoom)
    for x in range(0, zoom.width, 20):
        draw.line([(x,0),(x,zoom.height)], fill='red', width=1)
        draw.text((x+1,1), str(x+215), fill='red')
    for y in range(0, zoom.height, 20):
        draw.line([(0,y),(zoom.width,y)], fill='blue', width=1)
        draw.text((1,y+1), str(y+450), fill='blue')
    zoom.resize((zoom.width*3, zoom.height*3)).save(
        r'C:\claude\personal-website\screenshots\dropdown_y450.png')
    print("Saved dropdown_y450.png")
