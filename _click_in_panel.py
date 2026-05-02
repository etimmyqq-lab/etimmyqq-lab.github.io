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
time.sleep(0.3)

# Dialog panel: x=516 to 1360, content y=360+
# The "選取類型" row is in the left sub-panel of the dialog
# Try clicking at x=580 (well inside dialog), y=415 (type row area)
print("Clicking 選取類型 at (580, 415) — inside dialog panel...")
pyautogui.click(580, 415)
time.sleep(1.5)

img = pyautogui.screenshot()
# Crop just the dialog panel area (x=516 to 1360)
panel = img.crop((516, 330, 1360, 700))
draw = ImageDraw.Draw(panel)
for y in range(0, panel.height, 50):
    draw.line([(0, y), (panel.width, y)], fill='red', width=1)
    draw.text((2, y+2), str(y+330), fill='red')
for x in range(0, panel.width, 100):
    draw.line([(x, 0), (x, panel.height)], fill='red', width=1)
    draw.text((x+2, 2), str(x+516), fill='red')
panel.resize((panel.width//2, panel.height//2)).save(
    r'C:\claude\personal-website\screenshots\panel_click_result.png')

# Also check if dialog is still open (pixel at known dialog position)
r, g, b = np.array(img)[450, 700, :3]
print(f"Pixel at (700,450) after click: ({r},{g},{b}) — white means dialog still open")
print("Saved panel_click_result.png")
