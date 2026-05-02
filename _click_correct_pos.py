# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import win32gui, win32con
import time
import pyautogui
from PIL import Image, ImageDraw

pyautogui.PAUSE = 0.2
EDGE_HWND = 0x1509c0

win32gui.ShowWindow(EDGE_HWND, win32con.SW_RESTORE)
win32gui.SetForegroundWindow(EDGE_HWND)
time.sleep(0.3)

# "選取類型" row is at screen_y=344, screen_x≈140-200 based on dialog_left.png calibration
print("Clicking 選取類型 at (175, 344)...")
pyautogui.click(175, 344)
time.sleep(1.5)

img = pyautogui.screenshot()
dialog = img.crop((0, 250, 800, 700))
draw = ImageDraw.Draw(dialog)
for y in range(0, dialog.height, 50):
    draw.line([(0, y), (dialog.width, y)], fill='red', width=1)
    draw.text((2, y+2), str(y+250), fill='red')
for x in range(0, dialog.width, 50):
    draw.line([(x, 0), (x, dialog.height)], fill='red', width=1)
    draw.text((x+2, 2), str(x), fill='red')
dialog.resize((dialog.width, dialog.height)).save(
    r'C:\claude\personal-website\screenshots\selecttype_result.png')
print("Saved")
