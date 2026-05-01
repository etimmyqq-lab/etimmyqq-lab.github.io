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
    time.sleep(0.6)

# Get Edge window rect
rect = win32gui.GetWindowRect(EDGE_HWND)
print(f"Edge window rect: {rect}")  # (left, top, right, bottom)
wx, wy, wr, wb = rect
print(f"Window size: {wr-wx} x {wb-wy}")

bring_to_front()

# Navigate directly to the spreadsheet using address bar
pyautogui.hotkey('ctrl', 'l')
time.sleep(0.4)
pyautogui.hotkey('ctrl', 'a')
pyautogui.typewrite('https://docs.google.com/spreadsheets/d/12cbr5HMy4upCBOMbSO-DHYpRtMl1m_p8a2Lj2c8PJ2/edit', interval=0.02)
pyautogui.press('enter')
time.sleep(3.0)  # Wait for Sheets to load

# Take screenshot to see what's on screen and measure positions
img = pyautogui.screenshot()
img.save(r'C:\claude\personal-website\screenshots\sheets_loaded.png')
print("Sheets loaded screenshot saved")

# Check window title
print("Title:", win32gui.GetWindowText(EDGE_HWND))
