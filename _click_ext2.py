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
time.sleep(0.5)

pyautogui.press('escape')
time.sleep(0.4)

# "擴充功能" is to the left of "說明" (which was at x≈680)
# Try x=610 y=400
print("Clicking 擴充功能 at (610, 400)...")
pyautogui.click(610, 400)
time.sleep(1.2)

img = pyautogui.screenshot()
crop = img.crop((450, 390, 850, 650))
crop.resize((crop.width*2, crop.height*2)).save(r'C:\claude\personal-website\screenshots\drop2.png')
print("Done")
