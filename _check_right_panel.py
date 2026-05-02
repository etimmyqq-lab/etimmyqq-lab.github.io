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

# Save the FULL dialog (both panels combined) with clear labeling
full = img.crop((215, 360, 1370, 1140))
draw = ImageDraw.Draw(full)
# Vertical lines every 100px with labels
for x in range(0, full.width, 100):
    draw.line([(x, 0), (x, full.height)], fill='blue', width=1)
    draw.text((x+2, 2), str(x+215), fill='blue')
# Horizontal lines every 100px
for y in range(0, full.height, 100):
    draw.line([(0, y), (full.width, y)], fill='blue', width=1)
    draw.text((2, y+2), str(y+360), fill='blue')
full.resize((full.width//2, full.height//2)).save(
    r'C:\claude\personal-website\screenshots\full_dialog_annotated.png')
print("Saved full_dialog_annotated.png")
