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
    time.sleep(0.4)

bring_to_front()

# Close any open menu
pyautogui.press('escape')
time.sleep(0.4)
pyautogui.press('escape')
time.sleep(0.4)

# Get screen dimensions
sw, sh = pyautogui.size()
print(f"Screen: {sw}x{sh}")

# Take screenshot to find the Sheets menu bar
img = pyautogui.screenshot()
img.save(r'C:\claude\personal-website\screenshots\clean_sheet.png')

# The Google Sheets menu bar appears at a fixed position
# Menu bar row is about 10% from top of browser content area
# Browser chrome (address bar etc.) takes ~140px at 1.5x scale
# Spreadsheet menu bar is about 10px below that
# 擴充功能 is the 8th menu item

# Find "擴充功能" by looking at the menu bar area and clicking
# Based on typical Google Sheets layout at 1.5x scale (display scale detected from earlier)
# Browser window starts after taskbar (~40px from bottom)
# Let's use pyautogui.locateOnScreen approach with colors/patterns

# Try clicking approximate position of 擴充功能 menu
# At 1920x1080 scaled to 1.5 = 2880x1620 logical...
# Actually pyautogui uses logical pixels matching screen resolution

# From screenshot, menu bar items are at about y=130 (with browser tabs ~45, address bar ~30, bookmarks ~25, sheets menu ~130)
# 擴充功能 position (8th item): roughly x=675 at 1920 width
# Adjust proportionally

menu_y = int(sh * 0.118)  # ~12% from top
ext_x = int(sw * 0.352)   # 擴充功能 is roughly at 35% from left

print(f"Clicking 擴充功能 at ({ext_x}, {menu_y})")
pyautogui.click(ext_x, menu_y)
time.sleep(1.0)

img = pyautogui.screenshot()
img.save(r'C:\claude\personal-website\screenshots\ext_menu.png')
print("Extension menu screenshot saved")
