# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import win32gui, win32con
import time
import pyautogui
from PIL import Image

pyautogui.PAUSE = 0.1
EDGE_HWND = 0x1509c0

win32gui.ShowWindow(EDGE_HWND, win32con.SW_RESTORE)
win32gui.SetForegroundWindow(EDGE_HWND)
time.sleep(0.4)

img = pyautogui.screenshot()

# Save strips at different y ranges to find the Sheets menu bar
for y_start in range(300, 550, 30):
    crop = img.crop((0, y_start, 800, y_start + 30))
    zoomed = crop.resize((crop.width * 2, crop.height * 3))
    zoomed.save(rf'C:\claude\personal-website\screenshots\strip_{y_start}.png')

print("Strips saved, scan from y=300 to y=540")
