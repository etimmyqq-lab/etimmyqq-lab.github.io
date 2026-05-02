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

# From full_dialog_annotated.png: "選取類型" row at screen_y≈394
# Gear icon ⚙ at screen_x≈405, y≈394
# "選取類型" text at screen_x≈285, y≈394

print("Clicking gear ⚙ at (405, 394)...")
pyautogui.click(405, 394)
time.sleep(1.5)

img = pyautogui.screenshot()
r, g, b = np.array(img)[450, 700, :3]
dialog_open = r > 240 and g > 240 and b > 240
print(f"Dialog open: {dialog_open} (pixel at 700,450: {r},{g},{b})")

full = img.crop((215, 360, 1370, 700))
draw = ImageDraw.Draw(full)
for x in range(0, full.width, 100):
    draw.line([(x, 0), (x, full.height)], fill='red', width=1)
    draw.text((x+2, 2), str(x+215), fill='red')
for y in range(0, full.height, 50):
    draw.line([(0, y), (full.width, y)], fill='red', width=1)
    draw.text((2, y+2), str(y+360), fill='red')
full.resize((full.width//2, full.height//2)).save(
    r'C:\claude\personal-website\screenshots\gear_click_result.png')
print("Saved")
