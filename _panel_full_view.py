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

# Full dialog panel from top to bottom
panel = img.crop((516, 270, 1360, 1150))
draw = ImageDraw.Draw(panel)
for y in range(0, panel.height, 100):
    draw.line([(0, y), (panel.width, y)], fill='red', width=1)
    draw.text((2, y+2), str(y+270), fill='red')
for x in range(0, panel.width, 100):
    draw.line([(x, 0), (x, panel.height)], fill='red', width=1)
    draw.text((x+2, 2), str(x+516), fill='red')
panel.resize((panel.width//2, panel.height//2)).save(
    r'C:\claude\personal-website\screenshots\panel_full.png')
print("Saved panel_full.png")
