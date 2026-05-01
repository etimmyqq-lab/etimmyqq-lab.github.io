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
time.sleep(0.5)

# Escape any open menus/panels first
pyautogui.press('escape')
time.sleep(0.3)

# Click "擴充功能" at (680, 400)
print("Clicking 擴充功能...")
pyautogui.click(680, 400)
time.sleep(1.2)

img = pyautogui.screenshot()
img.save(r'C:\claude\personal-website\screenshots\click_ext.png')

# Crop the dropdown area to see what appeared
crop = img.crop((500, 390, 900, 600))
crop.resize((crop.width*2, crop.height*2)).save(r'C:\claude\personal-website\screenshots\dropdown.png')
print("Screenshot saved")
print("Title:", win32gui.GetWindowText(EDGE_HWND)[:60])
