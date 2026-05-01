# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import win32gui, win32con
import time
import pyautogui
from PIL import Image, ImageDraw

pyautogui.PAUSE = 0.15
EDGE_HWND = 0x1509c0

win32gui.ShowWindow(EDGE_HWND, win32con.SW_RESTORE)
win32gui.SetForegroundWindow(EDGE_HWND)
time.sleep(0.3)

img = pyautogui.screenshot()

# Print pyautogui screen size to check DPI
sz = pyautogui.size()
print(f"pyautogui screen size: {sz}")
print(f"Screenshot size: {img.size}")

# The Apps Script header bar — full width, y=330-400
header = img.crop((900, 330, 1600, 420))
header.save(r'C:\claude\personal-website\screenshots\header_raw.png')

# Draw a marker grid so we can calibrate x positions
draw = ImageDraw.Draw(header)
for x in range(0, header.width, 50):
    draw.line([(x, 0), (x, header.height)], fill='red', width=1)
    draw.text((x, 0), str(x+900), fill='red')
header.resize((header.width*2, header.height*2)).save(
    r'C:\claude\personal-website\screenshots\header_grid.png')

print("Saved header_grid.png")
