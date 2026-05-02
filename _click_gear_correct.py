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

def snap(tag, y0=390, y1=650):
    img = pyautogui.screenshot()
    arr = np.array(img)
    r, g, b = arr[450, 700, :3]
    alive = r > 240 and g > 240 and b > 240
    crop = img.crop((215, y0, 520, y1))
    draw = ImageDraw.Draw(crop)
    for x in range(0, crop.width, 20):
        col = 'red' if x % 100 == 0 else 'pink'
        draw.line([(x,0),(x,crop.height)], fill=col, width=1)
        if x % 20 == 0:
            draw.text((x+1,1), str(x+215), fill='red')
    for y in range(0, crop.height, 20):
        col = 'red' if y % 100 == 0 else 'pink'
        draw.line([(0,y),(crop.width,y)], fill=col, width=1)
        if y % 20 == 0:
            draw.text((1,y+1), str(y+y0), fill='blue')
    crop.resize((crop.width*3, crop.height*3)).save(
        f'C:\\claude\\personal-website\\screenshots\\{tag}.png')
    return alive, img

print("Gear is at ~(488, 472). Clicking gear...")
pyautogui.click(488, 472)
time.sleep(1.2)

alive, img = snap('gear488_result')
print(f"Dialog alive: {alive}")

if alive:
    # Scan for dropdown items below gear row (y=486-620)
    arr = np.array(img)
    print("Scanning y=486-620 for dropdown items:")
    for sy in range(486, 620, 4):
        row = arr[sy, 230:510, :]
        avg = row.mean()
        if avg < 240:
            print(f"  y={sy}: brightness={avg:.1f}")

    print("\nIf dropdown appeared, it would show new dark bands.")
    print("Zoomed view saved as gear488_result.png")
else:
    print("Dialog closed - click was outside dialog bounds")
