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

# Click the gear icon "設定" to open the type selector
# Gear icon is at approx screen (940, 735) based on dialog position
print("Clicking gear/settings icon at (940, 735)...")
pyautogui.click(940, 735)
time.sleep(1.5)

img = pyautogui.screenshot()
# Crop the dialog area
dialog = img.crop((400, 300, 1200, 1050))
dialog.save(r'C:\claude\personal-website\screenshots\type_selector.png')
print("Screenshot saved")
