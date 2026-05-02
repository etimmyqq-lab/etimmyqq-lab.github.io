# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import win32gui, win32con
import time
import pyautogui
import numpy as np
from PIL import Image, ImageDraw

pyautogui.PAUSE = 0.05  # Very fast
EDGE_HWND = 0x1509c0

win32gui.ShowWindow(EDGE_HWND, win32con.SW_RESTORE)
win32gui.SetForegroundWindow(EDGE_HWND)
time.sleep(0.4)

def snap(tag, y0=390, y1=640):
    img = pyautogui.screenshot()
    arr = np.array(img)
    r, g, b = arr[450, 700, :3]
    alive = r > 240 and g > 240 and b > 240
    crop = img.crop((215, y0, 520, y1))
    draw = ImageDraw.Draw(crop)
    for x in range(0, crop.width, 20):
        draw.line([(x,0),(x,crop.height)], fill='red', width=1)
        draw.text((x+1,1), str(x+215), fill='red')
    for y in range(0, crop.height, 20):
        draw.line([(0,y),(crop.width,y)], fill='blue', width=1)
        draw.text((1,y+1), str(y+y0), fill='blue')
    crop.resize((crop.width*3, crop.height*3)).save(
        f'C:\\claude\\personal-website\\screenshots\\{tag}.png')
    return alive

# Gear is at (488, 473).
# From dropdown scan: new content appeared at y=490-538 when dropdown was open.
# "網頁應用程式" should be first item at approximately y=495-515, center y≈505
# x center of left panel: (215+514)/2 ≈ 365

# Strategy: hover gear → click gear → IMMEDIATELY click 網頁應用程式
# Try multiple y positions for the first dropdown item

for item_y in [500, 495, 505, 490, 510]:
    print(f"\n--- Try: gear click then click item at y={item_y} ---")

    # Hover to activate gear
    pyautogui.moveTo(488, 473, duration=0.3)
    time.sleep(0.4)

    # Click gear
    pyautogui.click(488, 473)
    # NO sleep - immediately click the first item
    # "網頁應用程式" should be at approximately (365, item_y)
    pyautogui.click(365, item_y)
    time.sleep(0.8)

    img = pyautogui.screenshot()
    arr = np.array(img)
    dialog_open = arr[450, 700, :3].mean() > 240
    print(f"  Dialog open: {dialog_open}")

    if dialog_open:
        snap(f'fast_click_y{item_y}')
        # Check if right panel now shows 網路應用程式 config
        # Look for "網路應用程式" in right panel (we'd see different config options)
        # Check if left panel now shows 網頁應用程式 item
        left_panel = arr[490:540, 215:514, :]
        brightness = left_panel.mean()
        print(f"  Left panel y=490-540 brightness: {brightness:.1f}")
        if brightness < 235:
            print(f"  -> Dark content at y=490-540, dropdown may have item!")
        else:
            print(f"  -> Left panel white - check if type changed in right panel")

        # Check right panel for web app config marker
        # If 網路應用程式 selected, right panel shows different text
        right_top = arr[470:520, 520:900, :]
        print(f"  Right panel y=470-520 brightness: {right_top.mean():.1f}")
        snap(f'result_y{item_y}')
    else:
        print(f"  -> Dialog closed at y={item_y}")

    if not dialog_open:
        # Re-open dialog for next attempt
        pyautogui.click(1240, 375)
        time.sleep(1.2)
        pyautogui.click(1210, 435)
        time.sleep(2.0)
        print("  Re-opened dialog")

# Final state
print("\nFinal: checking current right panel config...")
img = pyautogui.screenshot()
crop = img.crop((520, 450, 1360, 700))
draw = ImageDraw.Draw(crop)
for x in range(0, crop.width, 100):
    draw.line([(x,0),(x,crop.height)], fill='red', width=1)
    draw.text((x+2,2), str(x+520), fill='red')
for y in range(0, crop.height, 50):
    draw.line([(0,y),(crop.width,y)], fill='red', width=1)
    draw.text((2,y+2), str(y+450), fill='red')
crop.resize((crop.width//2, crop.height//2)).save(
    r'C:\claude\personal-website\screenshots\right_panel_final.png')
print("Saved right_panel_final.png")
