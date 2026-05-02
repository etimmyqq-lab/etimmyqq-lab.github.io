# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import win32gui, win32con
import time
import pyautogui
from PIL import Image, ImageDraw

pyautogui.PAUSE = 0.2
EDGE_HWND = 0x1509c0

win32gui.ShowWindow(EDGE_HWND, win32con.SW_RESTORE)
win32gui.SetForegroundWindow(EDGE_HWND)
time.sleep(0.3)

# Click "選取類型" text at correct calibrated position: screen (285, 455)
print("Clicking 選取類型 text at (285, 455)...")
pyautogui.click(285, 455)
time.sleep(1.0)

img = pyautogui.screenshot()
left = img.crop((200, 330, 520, 600))
draw = ImageDraw.Draw(left)
for y in range(0, left.height, 50):
    draw.line([(0, y), (left.width, y)], fill='red', width=1)
    draw.text((2, y+2), str(y+330), fill='red')
for x in range(0, left.width, 50):
    draw.line([(x, 0), (x, left.height)], fill='red', width=1)
    draw.text((x+2, 2), str(x+200), fill='red')
left.resize((left.width*2, left.height*2)).save(
    r'C:\claude\personal-website\screenshots\after_select_text.png')
print("Saved after_select_text.png")

# If still showing same view, try the gear icon at (490, 455)
time.sleep(0.5)
img2 = pyautogui.screenshot()
# Check if dialog still open
import numpy as np
r, g, b = np.array(img2)[455, 490, :3]
print(f"Pixel (490,455): ({r},{g},{b})")
print(f"Pixel (700,500): {np.array(img2)[500, 700, :3]}")
