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

# The dialog is at screen ~(126, 162) to (700, 532)
# The gear/settings row "設定" is at approx screen (240, 234)
# The main content gear placeholder is at screen (470, 370)
# Try clicking the "設定" row at top of dialog
print("Clicking 設定 gear row at (240, 234)...")
pyautogui.click(240, 234)
time.sleep(1.5)

img = pyautogui.screenshot()
w, h = img.size
crop = img.crop((60, 80, 760, 600))
crop.resize((crop.width//2, crop.height//2)).save(
    r'C:\claude\personal-website\screenshots\after_settings_click.png')
print("Saved")
