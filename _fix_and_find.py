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
    time.sleep(0.6)

def title():
    return win32gui.GetWindowText(EDGE_HWND)

# Step 1: Undo the accidental paste
bring_to_front(EDGE_HWND)
for _ in range(10):
    pyautogui.hotkey('ctrl', 'z')
    time.sleep(0.1)
print("Undone")

# Step 2: List ALL windows to find Apps Script (maybe different window)
all_wins = []
def cb(hwnd, _):
    if win32gui.IsWindowVisible(hwnd):
        t = win32gui.GetWindowText(hwnd)
        if t and len(t) > 2:
            all_wins.append((hwnd, t))
win32gui.EnumWindows(cb, None)
print("All windows:")
for h, t in all_wins:
    print(f"  {hex(h)} {t[:100]}")

# Step 3: Navigate to the Google Sheet and open Apps Script from there
# First go to the spreadsheet tab
bring_to_front(EDGE_HWND)
time.sleep(0.4)

# Cycle through tabs looking for the Google Sheets tab
print("\nLooking for Google Sheets tab...")
for i in range(12):
    t = title()
    print(f"  {i}: {t[:80]}")
    if '試算表' in t or 'Sheet' in t.lower() or 'spreadsheet' in t.lower():
        print("  -> Found Sheets tab!")
        break
    pyautogui.hotkey('ctrl', 'tab')
    time.sleep(0.6)

# Take screenshot to see current state
img = pyautogui.screenshot()
img.save(r'C:\claude\personal-website\screenshots\current_state.png')
print("Screenshot saved")
