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
time.sleep(0.3)

img = pyautogui.screenshot()

# Zoom into the access dropdown area with fine grid
zoom = img.crop((520, 930, 1360, 1080))
draw = ImageDraw.Draw(zoom)
for x in range(0, zoom.width, 20):
    col = 'red' if x % 100 == 0 else 'pink'
    draw.line([(x,0),(x,zoom.height)], fill=col, width=1)
    if x % 40 == 0:
        draw.text((x+1,1), str(x+520), fill='red')
for y in range(0, zoom.height, 10):
    col = 'red' if y % 50 == 0 else 'pink'
    draw.line([(0,y),(zoom.width,y)], fill=col, width=1)
    if y % 20 == 0:
        draw.text((1,y+1), str(y+930), fill='blue')
zoom.resize((zoom.width*2, zoom.height*2)).save(
    r'C:\claude\personal-website\screenshots\access_zoom.png')
print("Saved access_zoom.png")

# Also scan for the dropdown element
arr = np.array(img)
print("Scanning right panel y=900-1100 for text/elements:")
for sy in range(900, 1100, 5):
    row = arr[sy, 530:1340, :]
    avg = row.mean()
    if avg < 245:
        print(f"  y={sy}: brightness={avg:.1f}")
