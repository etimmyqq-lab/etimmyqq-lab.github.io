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

# Zoom into just the "選取類型" row area at 4x magnification
# Row is at y≈385-415, spanning full dialog width x=215-1370
row = img.crop((215, 382, 900, 415))
row.resize((row.width*4, row.height*4)).save(
    r'C:\claude\personal-website\screenshots\selecttype_zoom.png')

# Also zoom in on the full first ~150px of dialog
top = img.crop((215, 358, 1370, 520))
draw = ImageDraw.Draw(top)
for x in range(0, top.width, 50):
    draw.line([(x,0),(x,top.height)], fill='red', width=1)
    draw.text((x+2, 2), str(x+215), fill='red')
for y in range(0, top.height, 20):
    draw.line([(0,y),(top.width,y)], fill='red', width=1)
    draw.text((2, y+2), str(y+358), fill='red')
top.resize((top.width//2, top.height//2)).save(
    r'C:\claude\personal-website\screenshots\dialog_top_zoom.png')

print("Saved zoom images")
