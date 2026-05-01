# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import win32gui, win32con
import time
import pyautogui
from PIL import Image

pyautogui.PAUSE = 0.1
EDGE_HWND = 0x1509c0

def bring_to_front():
    win32gui.ShowWindow(EDGE_HWND, win32con.SW_RESTORE)
    win32gui.SetForegroundWindow(EDGE_HWND)
    time.sleep(0.5)

bring_to_front()

# Ctrl+Z many times to undo the paste in the spreadsheet
print("Undoing paste in spreadsheet...")
for _ in range(15):
    pyautogui.hotkey('ctrl', 'z')
    time.sleep(0.15)

time.sleep(0.5)
img = pyautogui.screenshot()
img.save(r'C:\claude\personal-website\screenshots\after_undo.png')
print("Undo done, screenshot saved")

# Now open Apps Script from the menu: 擴充功能 → Apps Script
print("Opening Apps Script via menu...")
time.sleep(0.5)

# Click on 擴充功能 menu (Extensions menu)
# First, find where the menu is - it's in the spreadsheet toolbar
# Use keyboard: Alt to open menu bar
pyautogui.hotkey('alt', 'e')  # 擴充功能 shortcut in Google Sheets
time.sleep(0.5)

img = pyautogui.screenshot()
img.save(r'C:\claude\personal-website\screenshots\menu_open.png')
print("Menu opened, screenshot saved")
