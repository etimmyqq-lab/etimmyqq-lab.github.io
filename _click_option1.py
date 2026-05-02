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

def zoom_access(tag):
    img = pyautogui.screenshot()
    zoom = img.crop((520, 880, 1360, 1000))
    draw = ImageDraw.Draw(zoom)
    for x in range(0, zoom.width, 100):
        draw.line([(x,0),(x,zoom.height)], fill='red', width=1)
        draw.text((x+2,2), str(x+520), fill='red')
    for y in range(0, zoom.height, 10):
        col = 'red' if y % 50 == 0 else 'pink'
        draw.line([(0,y),(zoom.width,y)], fill=col, width=1)
        draw.text((2,y+2), str(y+880), fill='blue')
    zoom.save(f'C:\\claude\\personal-website\\screenshots\\{tag}.png')
    return img

# Open dropdown
print("Opening dropdown...")
pyautogui.click(800, 928)
time.sleep(0.6)

zoom_access('before_click_opt1')

# Click first option at y=973 (bright=127 = text at first item)
print("Clicking first option at (800, 973)...")
pyautogui.click(800, 973)
time.sleep(0.6)

img = zoom_access('after_opt1')
arr = np.array(img)

# Check what's now showing in the dropdown field (y=920-940)
text_row = arr[930, 530:1300, :]
print(f"Selected value text row brightness: {text_row.mean():.1f}")

# Save close-up of selected value
val = img.crop((520, 890, 1340, 960))
val.resize((val.width, val.height*4)).save(
    r'C:\claude\personal-website\screenshots\selected_val.png')
print("Saved selected_val.png")

# Open dropdown again to see all options clearly
print("Re-opening dropdown for full view...")
pyautogui.click(800, 928)
time.sleep(0.6)
img2 = pyautogui.screenshot()
all_opts = img2.crop((520, 955, 1340, 1035))
all_opts.resize((all_opts.width, all_opts.height*5)).save(
    r'C:\claude\personal-website\screenshots\all_options.png')
print("Saved all_options.png")

# Close dropdown with Escape
pyautogui.press('escape')
time.sleep(0.3)
