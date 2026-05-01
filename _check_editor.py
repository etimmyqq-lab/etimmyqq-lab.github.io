# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import win32gui, win32con
import time
import pyautogui
from PIL import Image

pyautogui.PAUSE = 0.15
EDGE_HWND = 0x1509c0

win32gui.ShowWindow(EDGE_HWND, win32con.SW_RESTORE)
win32gui.SetForegroundWindow(EDGE_HWND)
time.sleep(0.4)

img = pyautogui.screenshot()

# Crop just the editor code area (top portion showing lines 1-15)
# Edge window content y starts at ~280
# Apps Script editor code area is roughly y=460-1000
# Show top of code (y=460-650) to see lines 1-15
code_top = img.crop((100, 460, 900, 680))
code_top.resize((code_top.width*2, code_top.height*2)).save(
    r'C:\claude\personal-website\screenshots\code_top.png')

# Also crop the error bar at bottom
error_bar = img.crop((0, 1050, 1000, 1147))
error_bar.resize((error_bar.width*2, error_bar.height*2)).save(
    r'C:\claude\personal-website\screenshots\error_bar.png')

print("Screenshots saved")
