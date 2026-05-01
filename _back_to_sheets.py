# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import win32gui, win32con
import time
import pyautogui
from PIL import Image

pyautogui.PAUSE = 0.1
EDGE_HWND = 0x1509c0

# Window bounds from GetWindowRect: (-9, 161, 1587, 1147)
WIN_LEFT = -9
WIN_TOP = 161
WIN_RIGHT = 1587
WIN_BOTTOM = 1147
WIN_W = WIN_RIGHT - WIN_LEFT   # 1596
WIN_H = WIN_BOTTOM - WIN_TOP   # 986

def bring_to_front():
    win32gui.ShowWindow(EDGE_HWND, win32con.SW_RESTORE)
    win32gui.SetForegroundWindow(EDGE_HWND)
    time.sleep(0.5)

bring_to_front()

# Go back (Alt+Left)
pyautogui.hotkey('alt', 'left')
time.sleep(2.5)

img = pyautogui.screenshot()
img.save(r'C:\claude\personal-website\screenshots\back1.png')
t = win32gui.GetWindowText(EDGE_HWND)
print(f"After back: {t[:60]}")

# If not on sheets yet, keep going back
if '試算表' not in t and 'Sheet' not in t:
    pyautogui.hotkey('alt', 'left')
    time.sleep(2.5)
    t = win32gui.GetWindowText(EDGE_HWND)
    print(f"After back2: {t[:60]}")

img = pyautogui.screenshot()
img.save(r'C:\claude\personal-website\screenshots\back2.png')
print("Screenshot saved")
