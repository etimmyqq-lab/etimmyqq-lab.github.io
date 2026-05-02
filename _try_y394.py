# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import win32gui, win32con
import time
import pyautogui
import numpy as np
from PIL import Image, ImageDraw

pyautogui.PAUSE = 0.3
EDGE_HWND = 0x1509c0

win32gui.ShowWindow(EDGE_HWND, win32con.SW_RESTORE)
win32gui.SetForegroundWindow(EDGE_HWND)
time.sleep(0.3)

def snap(tag):
    img = pyautogui.screenshot()
    r, g, b = np.array(img)[450, 700, :3]
    alive = r > 240 and g > 240 and b > 240
    row = img.crop((215, 360, 1370, 560))
    draw = ImageDraw.Draw(row)
    for x in range(0, row.width, 100):
        draw.line([(x,0),(x,row.height)], fill='red', width=1)
        draw.text((x+2,2), str(x+215), fill='red')
    row.resize((row.width//2, row.height//2)).save(
        f'C:\\claude\\personal-website\\screenshots\\{tag}.png')
    return alive

# Try clicking at y=394 across different x positions
for x_pos in [250, 285, 340, 405, 460, 550, 650, 750]:
    print(f"Clicking ({x_pos}, 394)...")
    pyautogui.click(x_pos, 394)
    time.sleep(1.2)
    alive = snap(f'click_{x_pos}_394')
    if not alive:
        print(f"  -> Dialog CLOSED at x={x_pos}!")
        break
    # Save current state screenshot
    img = pyautogui.screenshot()
    changed = img.crop((215, 360, 1370, 700))
    changed.resize((changed.width//2, changed.height//2)).save(
        f'C:\\claude\\personal-website\\screenshots\\state_{x_pos}.png')
    print(f"  -> Dialog still open, saved state_{x_pos}.png")
