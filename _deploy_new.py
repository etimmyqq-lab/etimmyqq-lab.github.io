# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import win32gui, win32con
import time
import pyautogui
from PIL import Image

pyautogui.PAUSE = 0.2
EDGE_HWND = 0x1509c0

win32gui.ShowWindow(EDGE_HWND, win32con.SW_RESTORE)
win32gui.SetForegroundWindow(EDGE_HWND)
time.sleep(0.3)

# Click "新增部署作業" in the dropdown
print("Clicking 新增部署作業 at (1210, 435)...")
pyautogui.click(1210, 435)
time.sleep(3.0)  # dialog takes a moment to open

img = pyautogui.screenshot()
img.save(r'C:\claude\personal-website\screenshots\deploy_dialog_full.png')

# Crop center of screen where dialog likely appeared
dialog = img.crop((400, 300, 1600, 1000))
dialog.resize((dialog.width, dialog.height)).save(
    r'C:\claude\personal-website\screenshots\deploy_dialog.png')
print("Screenshot saved")
