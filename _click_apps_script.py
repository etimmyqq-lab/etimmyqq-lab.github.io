# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import win32gui, win32con
import time
import pyautogui
from PIL import Image

pyautogui.PAUSE = 0.15
EDGE_HWND = 0x1509c0

win32gui.ShowWindow(EDGE_HWND, win32con.SW_RESTORE)
win32gui.SetForegroundWindow(EDGE_HWND)
time.sleep(0.3)

# From the dropdown, "Apps Script" appears at approximately:
# crop was (450, 390, 850, 650), zoomed 2x = 800x520
# "Apps Script" row is at approximately y=310 in the 520px zoomed image
#   → y in crop = 310/2 = 155 → logical y = 390 + 155 = 545
# x center is approximately x=500 in the 800px image
#   → x in crop = 500/2 = 250 → logical x = 450 + 250 = 700
print("Clicking Apps Script at (700, 545)...")
pyautogui.click(700, 545)
time.sleep(3.0)  # wait for Apps Script to open in new tab

img = pyautogui.screenshot()
img.save(r'C:\claude\personal-website\screenshots\apps_script_opened.png')
title = win32gui.GetWindowText(EDGE_HWND)
print(f"Title: {title[:80]}")
