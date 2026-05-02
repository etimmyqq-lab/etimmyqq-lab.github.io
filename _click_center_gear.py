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

# Big center gear icon at screen (960, 840) based on full_dialog.png grid
print("Clicking center gear icon at (960, 840)...")
pyautogui.click(960, 840)
time.sleep(1.5)

img = pyautogui.screenshot()
# Wide crop to catch any dropdown or state change
dialog = img.crop((200, 380, 1400, 1100))
draw = ImageDraw.Draw(dialog)
for y in range(0, dialog.height, 100):
    draw.line([(0, y), (dialog.width, y)], fill='red', width=1)
    draw.text((2, y+2), str(y+380), fill='red')
for x in range(0, dialog.width, 200):
    draw.line([(x, 0), (x, dialog.height)], fill='red', width=1)
    draw.text((x+2, 2), str(x+200), fill='red')
dialog.resize((dialog.width//2, dialog.height//2)).save(
    r'C:\claude\personal-website\screenshots\after_gear_click.png')
print("Saved")
