# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import win32gui, win32con
import time
import pyautogui

pyautogui.PAUSE = 0.15
EDGE_HWND = 0x1509c0

win32gui.ShowWindow(EDGE_HWND, win32con.SW_RESTORE)
win32gui.SetForegroundWindow(EDGE_HWND)
time.sleep(0.3)

img = pyautogui.screenshot()

# Top toolbar area where Deploy button should be
toolbar = img.crop((0, 270, 1600, 430))
toolbar.resize((toolbar.width*2, toolbar.height*2)).save(
    r'C:\claude\personal-website\screenshots\toolbar.png')

# Also save the full top area
top = img.crop((0, 270, 1600, 550))
top.save(r'C:\claude\personal-website\screenshots\full_top.png')

print("Saved")
