# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import win32gui, win32con
import time
import pyautogui
from PIL import Image

pyautogui.PAUSE = 0.1

# Close the "另存新檔" dialog window
SAVEAS_HWND = 0x9d0a52
try:
    win32gui.PostMessage(SAVEAS_HWND, win32con.WM_CLOSE, 0, 0)
    print("Closed 另存新檔 dialog")
except Exception as e:
    print(f"Close failed: {e}")

time.sleep(0.5)

# Bring Edge to front
EDGE_HWND = 0x1509c0
win32gui.ShowWindow(EDGE_HWND, win32con.SW_RESTORE)
win32gui.SetForegroundWindow(EDGE_HWND)
time.sleep(0.8)

img = pyautogui.screenshot()
img.save(r'C:\claude\personal-website\screenshots\after_close.png')
print("Screenshot saved")
