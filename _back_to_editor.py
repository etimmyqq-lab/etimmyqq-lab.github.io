# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import win32gui, win32con
import time
import pyautogui
import numpy as np
from PIL import Image, ImageDraw

pyautogui.PAUSE = 0.2
EDGE_HWND = 0x1509c0

win32gui.ShowWindow(EDGE_HWND, win32con.SW_RESTORE)
win32gui.SetForegroundWindow(EDGE_HWND)
time.sleep(0.4)

def full_snap(tag):
    img = pyautogui.screenshot()
    crop = img.crop((0, 0, 1400, 800))
    crop.resize((700, 400)).save(
        f'C:\\claude\\personal-website\\screenshots\\{tag}.png')
    return img

print("Current state...")
full_snap('back_before')

# Try pressing Escape to close any popup/dialog
print("Pressing Escape...")
pyautogui.press('escape')
time.sleep(0.8)
full_snap('after_escape')

# Try browser back button
print("Pressing Alt+Left (browser back)...")
pyautogui.hotkey('alt', 'left')
time.sleep(1.5)
full_snap('after_back')

# Take a look at what tabs are open
img = pyautogui.screenshot()
# Check the tab bar area (y≈50-90 on 2560x1440 screen)
tab_area = img.crop((0, 50, 1400, 95))
tab_area.resize((700, 45)).save(
    r'C:\claude\personal-website\screenshots\tab_bar.png')
print("Saved tab_bar.png")

# Full current view
full_snap('current_view')
print("Saved current_view.png")
