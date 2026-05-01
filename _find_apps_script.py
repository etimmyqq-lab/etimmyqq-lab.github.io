# -*- coding: utf-8 -*-
"""
Cycle through Edge tabs to find the Apps Script editor,
then paste the code from clipboard and save.
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

import win32gui
import win32con
import win32api
import time
import pyautogui
from PIL import Image

pyautogui.PAUSE = 0.1

EDGE_HWND = 0x1509c0  # "昆廷老師需求表單 - Google 試算表 和其他 7 個頁面 - Edge"

def bring_to_front(hwnd):
    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
    win32gui.SetForegroundWindow(hwnd)
    time.sleep(0.6)

def send_keys(*keys):
    for k in keys:
        pyautogui.hotkey(*k) if isinstance(k, tuple) else pyautogui.press(k)
        time.sleep(0.15)

def get_screenshot():
    return pyautogui.screenshot()

def title_on_tab():
    """Read current window title - Edge updates it to reflect active tab."""
    return win32gui.GetWindowText(EDGE_HWND)

bring_to_front(EDGE_HWND)
time.sleep(0.5)

# Cycle through all tabs to find Apps Script
print("Searching tabs for Apps Script...")
found = False
for i in range(10):
    title = title_on_tab()
    print(f"  Tab {i}: {title[:80]}")
    if "script" in title.lower() or "Apps Script" in title or "Script" in title:
        print(f"  -> Found Apps Script tab!")
        found = True
        break
    pyautogui.hotkey('ctrl', 'tab')
    time.sleep(0.7)

if not found:
    # Try going back to first tab and using Ctrl+Shift+A (tab search in Edge)
    print("Not found by cycling. Trying tab search...")
    bring_to_front(EDGE_HWND)
    pyautogui.hotkey('ctrl', 'shift', 'a')
    time.sleep(0.5)
    pyautogui.write('Apps Script', interval=0.05)
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.8)

# Take screenshot to verify
img = get_screenshot()
img.save(r'C:\claude\personal-website\screenshots\tab_check.png')
print(f"Screenshot saved. Current title: {title_on_tab()[:80]}")

# Now paste - click in the middle of screen (editor area)
screen_w, screen_h = pyautogui.size()
# Apps Script editor is roughly center-right area
editor_x = int(screen_w * 0.55)
editor_y = int(screen_h * 0.5)
pyautogui.click(editor_x, editor_y)
time.sleep(0.4)

# Select all and paste
pyautogui.hotkey('ctrl', 'a')
time.sleep(0.3)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.6)

# Save
pyautogui.hotkey('ctrl', 's')
time.sleep(0.8)

# Take final screenshot
img = get_screenshot()
img.save(r'C:\claude\personal-website\screenshots\after_paste.png')
print("Done! Code pasted and saved.")
