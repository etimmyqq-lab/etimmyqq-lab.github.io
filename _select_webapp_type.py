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

# Click "選取類型" dropdown in the deployment dialog
# screen_x=300 (dropdown text), screen_y=466 (the type selector row)
print("Clicking 選取類型 at (300, 466)...")
pyautogui.click(300, 466)
time.sleep(1.2)

img = pyautogui.screenshot()
# Crop the dialog area after the click
dialog = img.crop((200, 380, 1000, 900))
draw = ImageDraw.Draw(dialog)
for y in range(0, dialog.height, 100):
    draw.line([(0, y), (dialog.width, y)], fill='red', width=1)
    draw.text((2, y+2), str(y+380), fill='red')
for x in range(0, dialog.width, 100):
    draw.line([(x, 0), (x, dialog.height)], fill='red', width=1)
    draw.text((x+2, 2), str(x+200), fill='red')
dialog.resize((dialog.width//2, dialog.height//2)).save(
    r'C:\claude\personal-website\screenshots\type_dropdown.png')
print("Saved")
