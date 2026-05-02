# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import win32gui, win32con
import time
import pyautogui
from PIL import Image, ImageDraw

pyautogui.PAUSE = 0.1
EDGE_HWND = 0x1509c0

win32gui.ShowWindow(EDGE_HWND, win32con.SW_RESTORE)
win32gui.SetForegroundWindow(EDGE_HWND)
time.sleep(0.3)

# Hover over "選取類型" row
print("Moving to 選取類型 at (285, 455)...")
pyautogui.moveTo(285, 455)
time.sleep(1.5)

# Take screenshot to see if hover state changed anything
img = pyautogui.screenshot()
left = img.crop((200, 430, 520, 510))
left.resize((left.width*3, left.height*3)).save(
    r'C:\claude\personal-website\screenshots\hover_state.png')

# Also take a wider view
wide = img.crop((200, 330, 520, 600))
draw = ImageDraw.Draw(wide)
for y in range(0, wide.height, 50):
    draw.line([(0, y), (wide.width, y)], fill='red', width=1)
    draw.text((2, y+2), str(y+330), fill='red')
wide.resize((wide.width*2, wide.height*2)).save(
    r'C:\claude\personal-website\screenshots\hover_wide.png')

print("Screenshots saved — inspecting hover state")

# Now click and take screenshot immediately
pyautogui.click()
time.sleep(0.8)
img3 = pyautogui.screenshot()
result = img3.crop((200, 330, 900, 700))
draw3 = ImageDraw.Draw(result)
for y in range(0, result.height, 50):
    draw3.line([(0, y), (result.width, y)], fill='red', width=1)
    draw3.text((2, y+2), str(y+330), fill='red')
for x in range(0, result.width, 100):
    draw3.line([(x, 0), (x, result.height)], fill='red', width=1)
    draw3.text((x+2, 2), str(x+200), fill='red')
result.resize((result.width//2, result.height//2)).save(
    r'C:\claude\personal-website\screenshots\after_hover_click.png')
print("After-click screenshot saved")
