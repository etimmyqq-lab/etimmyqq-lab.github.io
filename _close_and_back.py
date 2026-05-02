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
time.sleep(0.4)

def snap(tag):
    img = pyautogui.screenshot()
    img.crop((0, 50, 1400, 900)).resize((700, 425)).save(
        f'C:\\claude\\personal-website\\screenshots\\{tag}.png')
    return img

# Close this docs tab
print("Closing docs tab with Ctrl+W...")
pyautogui.hotkey('ctrl', 'w')
time.sleep(1.0)
snap('after_close_tab')

# Check where we are
img = pyautogui.screenshot()
arr = np.array(img)
# Read URL bar
url_crop = img.crop((250, 98, 900, 120))
url_crop.resize((650, 22)).save(r'C:\claude\personal-website\screenshots\url_bar.png')

# Wide view
img.crop((0, 50, 1400, 900)).resize((700, 425)).save(
    r'C:\claude\personal-website\screenshots\after_close_full.png')
print("Saved after_close_full.png and url_bar.png")
