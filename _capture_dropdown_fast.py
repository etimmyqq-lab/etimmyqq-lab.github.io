# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import win32gui, win32con
import time
import pyautogui
import numpy as np
from PIL import Image, ImageDraw

pyautogui.PAUSE = 0.05
EDGE_HWND = 0x1509c0

win32gui.ShowWindow(EDGE_HWND, win32con.SW_RESTORE)
win32gui.SetForegroundWindow(EDGE_HWND)
time.sleep(0.4)

# Hover gear then click to open dropdown, take screenshot FAST
print("Hovering gear...")
pyautogui.moveTo(488, 473, duration=0.3)
time.sleep(0.5)
print("Clicking gear and capturing dropdown state quickly...")
pyautogui.click(488, 473)

# Try multiple fast screenshots at different delays
for delay_ms in [100, 200, 300, 500, 800]:
    time.sleep(delay_ms / 1000.0)
    img = pyautogui.screenshot()
    arr = np.array(img)

    # Scan left panel for dropdown content
    dark_rows = []
    for sy in range(480, 620):
        row = arr[sy, 220:510, :]
        if row.mean() < 238:
            dark_rows.append(sy)

    if dark_rows:
        # Find the new dark rows (not the known "API 執行檔" at 537-553 and "資料庫" at 585-603)
        new_rows = [y for y in dark_rows if y < 530 or (557 < y < 580)]
        if new_rows:
            print(f"  t+{delay_ms}ms: NEW dark rows at y={new_rows[:10]}")
            # Save this frame!
            crop = img.crop((215, 460, 520, 650))
            draw = ImageDraw.Draw(crop)
            for x in range(0, crop.width, 20):
                draw.line([(x,0),(x,crop.height)], fill='red', width=1)
                draw.text((x+1,1), str(x+215), fill='red')
            for y in range(0, crop.height, 10):
                draw.line([(0,y),(crop.width,y)], fill='blue', width=1)
                draw.text((1,y+1), str(y+460), fill='blue')
            crop.resize((crop.width*4, crop.height*4)).save(
                f'C:\\claude\\personal-website\\screenshots\\dropdown_t{delay_ms}.png')
            print(f"  Saved dropdown_t{delay_ms}.png")
        else:
            print(f"  t+{delay_ms}ms: Known dark rows only at {dark_rows[:5]}...")
    else:
        print(f"  t+{delay_ms}ms: All white")

print("\nRe-hovering and clicking to open dropdown one more time for item scan...")
pyautogui.moveTo(488, 473, duration=0.3)
time.sleep(0.4)
pyautogui.click(488, 473)
time.sleep(0.25)  # Wait 250ms

img = pyautogui.screenshot()
arr = np.array(img)
print("Full left panel brightness scan (y=480-620):")
for sy in range(480, 625, 2):
    row = arr[sy, 220:510, :]
    avg = row.mean()
    if avg < 250:  # more sensitive threshold
        print(f"  y={sy}: {avg:.1f}", end="")
        if avg < 230:
            print(" <<<")
        else:
            print()
