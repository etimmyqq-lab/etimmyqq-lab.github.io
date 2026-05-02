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

# Click "選取類型" — try y=466 this time (from state_grid estimate)
print("Clicking 選取類型 at (260, 466)...")
pyautogui.click(260, 466)
time.sleep(1.0)

img = pyautogui.screenshot()
# Full dialog area with labels — cover y=380 to y=1100
dialog = img.crop((200, 380, 1100, 1100))
draw = ImageDraw.Draw(dialog)
for y in range(0, dialog.height, 100):
    draw.line([(0, y), (dialog.width, y)], fill='red', width=1)
    draw.text((2, y+2), str(y+380), fill='red')
for x in range(0, dialog.width, 100):
    draw.line([(x, 0), (x, dialog.height)], fill='red', width=1)
    draw.text((x+2, 2), str(x+200), fill='red')
dialog.resize((dialog.width//2, dialog.height//2)).save(
    r'C:\claude\personal-website\screenshots\full_dialog.png')
print("Saved full_dialog.png")
