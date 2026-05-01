# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import win32gui, win32con
import time
import pyautogui
from PIL import Image, ImageDraw

pyautogui.PAUSE = 0.2
EDGE_HWND = 0x1509c0

# Close address bar if open, bring Edge back
pyautogui.press('escape')
time.sleep(0.3)
win32gui.ShowWindow(EDGE_HWND, win32con.SW_RESTORE)
win32gui.SetForegroundWindow(EDGE_HWND)
time.sleep(0.5)

img = pyautogui.screenshot()

# Save center region with coordinate grid
center = img.crop((200, 300, 1400, 1100))
draw = ImageDraw.Draw(center)
for x in range(0, center.width, 100):
    draw.line([(x, 0), (x, center.height)], fill='red', width=1)
    draw.text((x+2, 2), str(x+200), fill='red')
for y in range(0, center.height, 100):
    draw.line([(0, y), (center.width, y)], fill='red', width=1)
    draw.text((2, y+2), str(y+300), fill='red')

center.resize((center.width//2, center.height//2)).save(
    r'C:\claude\personal-website\screenshots\state_grid.png')
print(f"Saved — title: {win32gui.GetWindowText(EDGE_HWND)[:60]}")
