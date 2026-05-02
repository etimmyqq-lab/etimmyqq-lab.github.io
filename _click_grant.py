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
time.sleep(0.4)

def snap_full(tag):
    img = pyautogui.screenshot()
    img.crop((0, 200, 1400, 1000)).resize((700, 400)).save(
        f'C:\\claude\\personal-website\\screenshots\\{tag}.png')
    return img

# Button center: x=(244+421)/2=332, y=(525+545)/2=535
print("Clicking '授予存取權' button at (332, 535)...")
pyautogui.click(332, 535)
time.sleep(3.0)

snap_full('after_grant_click')

# Check current state
img = pyautogui.screenshot()
arr = np.array(img)
print(f"Pixel at (700,450): {arr[450, 700, :3]}")

# Take wide screenshot to see full browser
img.crop((0, 0, 1400, 1000)).resize((700, 500)).save(
    r'C:\claude\personal-website\screenshots\state_after_grant.png')
print("Saved state_after_grant.png")
