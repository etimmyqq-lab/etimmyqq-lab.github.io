# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import win32gui, win32con
import time
import pyautogui
from PIL import Image

pyautogui.PAUSE = 0.1

EDGE_HWND = 0x1509c0

def bring_to_front(hwnd):
    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
    win32gui.SetForegroundWindow(hwnd)
    time.sleep(0.5)

# Close the Save As dialog with Escape
bring_to_front(EDGE_HWND)
pyautogui.press('escape')
time.sleep(0.5)

# Also close any other dialogs
pyautogui.press('escape')
time.sleep(0.3)

# Take screenshot to see current state
img = pyautogui.screenshot()
img.save(r'C:\claude\personal-website\screenshots\clean_state.png')
print("Screenshot saved")

# Print current window title
import win32gui
print("Current:", win32gui.GetWindowText(EDGE_HWND))
