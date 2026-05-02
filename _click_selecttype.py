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

# Try clicking "選取類型" dropdown at more precise position
# screen_x=260 (center of "選取類型" text), screen_y=436
print("Clicking 選取類型 at (260, 436)...")
pyautogui.click(260, 436)
time.sleep(1.5)

img = pyautogui.screenshot()
dialog = img.crop((200, 380, 1000, 700))
draw = ImageDraw.Draw(dialog)
for y in range(0, dialog.height, 100):
    draw.line([(0, y), (dialog.width, y)], fill='red', width=1)
    draw.text((2, y+2), str(y+380), fill='red')
for x in range(0, dialog.width, 100):
    draw.line([(x, 0), (x, dialog.height)], fill='red', width=1)
    draw.text((x+2, 2), str(x+200), fill='red')
dialog.resize((dialog.width//2, dialog.height//2)).save(
    r'C:\claude\personal-website\screenshots\after_type_click.png')
print("Saved")
