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

# Click in dialog to focus it first — use x=700 (right panel) y=600 (middle)
print("Clicking inside dialog to focus (700, 600)...")
pyautogui.click(700, 600)
time.sleep(0.4)

# Press Tab repeatedly and take screenshot after each
# Stop if dialog closes (then we overshot to Cancel)
for i in range(1, 9):
    pyautogui.press('tab')
    time.sleep(0.5)
    img = pyautogui.screenshot()

    import numpy as np
    r, g, b = np.array(img)[600, 700, :3]
    alive = r > 240 and g > 240 and b > 240

    snap = img.crop((215, 358, 1370, 700))
    draw = ImageDraw.Draw(snap)
    for x in range(0, snap.width, 100):
        draw.line([(x,0),(x,snap.height)], fill='red', width=1)
        draw.text((x+2, 2), str(x+215), fill='red')
    for y in range(0, snap.height, 50):
        draw.line([(0,y),(snap.width,y)], fill='red', width=1)
        draw.text((2, y+2), str(y+358), fill='red')
    snap.resize((snap.width//2, snap.height//2)).save(
        f'C:\\claude\\personal-website\\screenshots\\tab{i:02d}.png')

    print(f"Tab {i}: dialog_open={alive}")
    if not alive:
        print("  Dialog closed — hit cancel!")
        break
