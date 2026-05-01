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
time.sleep(0.5)

# Click the dropdown arrow ▼ on the 部署 button (calibrated from grid: x≈1240, y≈375)
print("Clicking 部署 ▼ dropdown at (1240, 375)...")
pyautogui.click(1240, 375)
time.sleep(1.5)

img = pyautogui.screenshot()
# Capture wide area below button to see the dropdown menu
dropdown = img.crop((1050, 370, 1500, 550))
dropdown.resize((dropdown.width*2, dropdown.height*2)).save(
    r'C:\claude\personal-website\screenshots\deploy_dropdown.png')
print("Screenshot saved")
