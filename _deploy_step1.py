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
time.sleep(0.4)

# Click the dropdown arrow on the blue "部署" button
# Toolbar is at screen y≈350-380; button right side (dropdown arrow) at x≈992
print("Clicking 部署 dropdown arrow at (992, 366)...")
pyautogui.click(992, 366)
time.sleep(1.5)

img = pyautogui.screenshot()
# Crop the area where the deploy dropdown menu should appear
menu_area = img.crop((800, 350, 1300, 550))
menu_area.resize((menu_area.width*2, menu_area.height*2)).save(
    r'C:\claude\personal-website\screenshots\deploy_menu.png')
print("Screenshot saved")
