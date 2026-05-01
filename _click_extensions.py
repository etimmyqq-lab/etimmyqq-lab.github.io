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
time.sleep(0.5)

# Edge window: (-9, 161, 1587, 1147) = roughly x:0~1587, y:161~1147
# Crop the menu bar area from the full screenshot
img = pyautogui.screenshot()

# Crop the Google Sheets menu bar area
# Browser chrome ~140px from window top=161 → content y≈300
# Sheets menu bar is first row of content, about 40px tall
crop = img.crop((0, 300, 1587, 360))
crop_scaled = crop.resize((crop.width * 2, crop.height * 4))  # zoom in for readability
crop_scaled.save(r'C:\claude\personal-website\screenshots\menubar_zoom.png')
print("Cropped menu bar saved")

# Also save the full sheet for reference
img.save(r'C:\claude\personal-website\screenshots\full_now.png')
