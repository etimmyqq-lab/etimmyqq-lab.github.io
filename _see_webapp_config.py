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

# Full dialog - extra tall to see all config options
full = img.crop((215, 358, 1370, 1100))
draw = ImageDraw.Draw(full)
for x in range(0, full.width, 100):
    draw.line([(x,0),(x,full.height)], fill='red', width=1)
    draw.text((x+2,2), str(x+215), fill='red')
for y in range(0, full.height, 50):
    col = 'red' if y % 100 == 0 else 'pink'
    draw.line([(0,y),(full.width,y)], fill=col, width=1)
    draw.text((2,y+2), str(y+358), fill='blue')
full.resize((full.width//2, full.height//2)).save(
    r'C:\claude\personal-website\screenshots\webapp_full_config.png')
print("Saved webapp_full_config.png")
