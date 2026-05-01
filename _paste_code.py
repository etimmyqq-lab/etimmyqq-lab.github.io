# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import win32gui, win32con
import time
import pyautogui
from PIL import Image

pyautogui.PAUSE = 0.15
EDGE_HWND = 0x1509c0

def bring_to_front():
    win32gui.ShowWindow(EDGE_HWND, win32con.SW_RESTORE)
    win32gui.SetForegroundWindow(EDGE_HWND)
    time.sleep(0.5)

bring_to_front()

# Wait for Apps Script to finish loading
print("Waiting for Apps Script to load...")
for i in range(20):
    t = win32gui.GetWindowText(EDGE_HWND)
    print(f"  {i}: {t[:60]}")
    if '正在建立' not in t and 'Apps Script' in t:
        print("  -> Loaded!")
        break
    time.sleep(1.5)

time.sleep(1.0)
img = pyautogui.screenshot()
img.save(r'C:\claude\personal-website\screenshots\as_loaded.png')
print("Screenshot saved")

# The Apps Script editor - click on the code editor area
# Apps Script editor typically occupies the right portion of the window
# Editor x: roughly center of the content, y: roughly middle
# Edge window: (-9, 161, 1587, 1147), content ≈ (0, 280, 1587, 1147)
# Editor code area: approximately x=500-1400, y=500-900
editor_x = 750
editor_y = 600
print(f"Clicking editor at ({editor_x}, {editor_y})...")
pyautogui.click(editor_x, editor_y)
time.sleep(0.5)

# Select all and paste
pyautogui.hotkey('ctrl', 'a')
time.sleep(0.4)
pyautogui.hotkey('ctrl', 'v')
time.sleep(1.0)

# Save with Ctrl+S
pyautogui.hotkey('ctrl', 's')
time.sleep(1.5)

img = pyautogui.screenshot()
img.save(r'C:\claude\personal-website\screenshots\as_pasted.png')
print("Pasted and saved")
t = win32gui.GetWindowText(EDGE_HWND)
print(f"Title: {t[:80]}")
