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

img = pyautogui.screenshot()

# Crop the LEFT PANEL of the dialog (x=200 to 520, y=330 to 1100)
left_panel = img.crop((200, 330, 520, 1100))
draw = ImageDraw.Draw(left_panel)
for y in range(0, left_panel.height, 50):
    draw.line([(0, y), (left_panel.width, y)], fill='red', width=1)
    draw.text((2, y+2), str(y+330), fill='red')
for x in range(0, left_panel.width, 50):
    draw.line([(x, 0), (x, left_panel.height)], fill='red', width=1)
    draw.text((x+2, 2), str(x+200), fill='red')
# Save at 2x for readability
left_panel.resize((left_panel.width*2, left_panel.height*2)).save(
    r'C:\claude\personal-website\screenshots\left_panel.png')
print("Saved left_panel.png")
