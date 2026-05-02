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

def snap(tag, y0=800, y1=1100):
    img = pyautogui.screenshot()
    crop = img.crop((215, y0, 1370, y1))
    draw = ImageDraw.Draw(crop)
    for x in range(0, crop.width, 100):
        draw.line([(x,0),(x,crop.height)], fill='red', width=1)
        draw.text((x+2,2), str(x+215), fill='red')
    for y in range(0, crop.height, 50):
        draw.line([(0,y),(crop.width,y)], fill='red', width=1)
        draw.text((2,y+2), str(y+y0), fill='blue')
    crop.resize((crop.width//2, crop.height//2)).save(
        f'C:\\claude\\personal-website\\screenshots\\{tag}.png')
    return img

# From webapp_full_config.png:
# "誰可以存取" label at screen y≈950-960
# "只有我自己" dropdown at screen y≈965-990, center≈975
# Right panel center x ≈ (520+1360)/2 = 940
# "部署" button at y≈1058, x≈1300 (right side)

print("Clicking '只有我自己' dropdown to change to '所有人'...")
pyautogui.click(930, 975)
time.sleep(1.0)
snap('dropdown_access')

# Take full view to see dropdown options
img = pyautogui.screenshot()
full = img.crop((215, 900, 1370, 1200))
draw = ImageDraw.Draw(full)
for x in range(0, full.width, 100):
    draw.line([(x,0),(x,full.height)], fill='red', width=1)
    draw.text((x+2,2), str(x+215), fill='red')
for y in range(0, full.height, 50):
    draw.line([(0,y),(full.width,y)], fill='red', width=1)
    draw.text((2,y+2), str(y+900), fill='blue')
full.resize((full.width//2, full.height//2)).save(
    r'C:\claude\personal-website\screenshots\access_dropdown_open.png')
print("Saved access_dropdown_open.png")
