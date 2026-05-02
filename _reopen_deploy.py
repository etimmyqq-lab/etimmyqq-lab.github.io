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
time.sleep(0.4)

# Click 部署 ▼ button (calibrated: x=1240, y=375)
print("Clicking 部署 ▼...")
pyautogui.click(1240, 375)
time.sleep(1.5)

# Click 新增部署作業 (calibrated: x=1210, y=435)
print("Clicking 新增部署作業...")
pyautogui.click(1210, 435)
time.sleep(3.0)

# Take screenshot immediately after dialog opens
img = pyautogui.screenshot()

# Save FULL right half of screen (dialog is likely there)
right_half = img.crop((800, 200, 2560, 1200))
draw = ImageDraw.Draw(right_half)
for y in range(0, right_half.height, 100):
    draw.line([(0, y), (right_half.width, y)], fill='red', width=1)
    draw.text((2, y+2), str(y+200), fill='red')
for x in range(0, right_half.width, 100):
    draw.line([(x, 0), (x, right_half.height)], fill='red', width=1)
    draw.text((x+2, 2), str(x+800), fill='red')
right_half.resize((right_half.width//3, right_half.height//3)).save(
    r'C:\claude\personal-website\screenshots\dialog_right.png')

# Also save left half
left_half = img.crop((0, 200, 1200, 1200))
draw2 = ImageDraw.Draw(left_half)
for y in range(0, left_half.height, 100):
    draw2.line([(0, y), (left_half.width, y)], fill='red', width=1)
    draw2.text((2, y+2), str(y+200), fill='red')
for x in range(0, left_half.width, 100):
    draw2.line([(x, 0), (x, left_half.height)], fill='red', width=1)
    draw2.text((x+2, 2), str(x), fill='red')
left_half.resize((left_half.width//2, left_half.height//2)).save(
    r'C:\claude\personal-website\screenshots\dialog_left.png')

print("Saved both halves")
print(f"Title: {win32gui.GetWindowText(EDGE_HWND)[:60]}")
