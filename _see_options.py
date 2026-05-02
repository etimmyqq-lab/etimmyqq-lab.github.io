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

# Click chevron again to open dropdown
print("Opening dropdown (clicking chevron area)...")
pyautogui.click(1290, 928)
time.sleep(0.8)

img = pyautogui.screenshot()

# Zoom into the dropdown LIST area y=955-1030 (options list)
zoom = img.crop((520, 955, 1360, 1035))
draw = ImageDraw.Draw(zoom)
for x in range(0, zoom.width, 100):
    draw.line([(x,0),(x,zoom.height)], fill='red', width=1)
    draw.text((x+2,2), str(x+520), fill='red')
for y in range(0, zoom.height, 10):
    col = 'red' if y % 30 == 0 else 'pink'
    draw.line([(0,y),(zoom.width,y)], fill=col, width=1)
    draw.text((2,y+2), str(y+955), fill='blue')
zoom.resize((zoom.width, zoom.height*3)).save(
    r'C:\claude\personal-website\screenshots\options_list.png')
print("Saved options_list.png")

# Also raw (no annotation) to see text clearly
raw = img.crop((520, 955, 1360, 1035))
raw.resize((raw.width, raw.height*4)).save(
    r'C:\claude\personal-website\screenshots\options_raw.png')
print("Saved options_raw.png")
