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

img = pyautogui.screenshot()

# Mark every 100px with grid lines and coordinate labels
draw = ImageDraw.Draw(img)
for x in range(0, img.width, 200):
    draw.line([(x, 0), (x, img.height)], fill='red', width=2)
    draw.text((x+2, 10), str(x), fill='red')
for y in range(0, img.height, 200):
    draw.line([(0, y), (img.width, y)], fill='red', width=2)
    draw.text((2, y+2), str(y), fill='red')

# Save scaled down
w, h = img.size
img.resize((w//2, h//2)).save(r'C:\claude\personal-website\screenshots\full_grid.png')
print(f"Saved full grid {w}x{h}")
