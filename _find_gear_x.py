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
time.sleep(0.3)

img = pyautogui.screenshot()
arr = np.array(img)

# Gear row is confirmed at y=394-418 from pixel scan.
# Scan x positions in this row to find the gear icon location
print("Horizontal scan of gear row (y=394-418):")
for sy in range(394, 419):
    row = arr[sy, 215:515, :]  # x=215-514 (left panel)
    # Find dark pixels (below 200 brightness)
    dark_mask = row.mean(axis=1) < 200
    dark_xs = np.where(dark_mask)[0] + 215  # screen x positions
    if len(dark_xs) > 0:
        print(f"  y={sy}: dark pixels at x={dark_xs[:5].tolist()}...{dark_xs[-5:].tolist() if len(dark_xs)>5 else ''} (count={len(dark_xs)})")

# Zoom into gear row
print("\nSaving gear row zoom...")
zoom = img.crop((215, 388, 520, 425))
draw = ImageDraw.Draw(zoom)
for x in range(0, zoom.width, 10):
    col = 'red' if x % 50 == 0 else 'pink'
    draw.line([(x,0),(x,zoom.height)], fill=col, width=1)
    if x % 20 == 0:
        draw.text((x+1,1), str(x+215), fill='red')
for y in range(0, zoom.height, 5):
    draw.line([(0,y),(zoom.width,y)], fill='blue', width=1)
    draw.text((1,y+1), str(y+388), fill='blue')
zoom.resize((zoom.width*4, zoom.height*4)).save(
    r'C:\claude\personal-website\screenshots\gear_row_zoom.png')
print("Saved gear_row_zoom.png")

# After identifying gear position, try clicking it
# Based on earlier analysis + scan: gear is likely at x≈395-415, y≈406
print("\nClicking gear at (405, 406)...")
pyautogui.click(405, 406)
time.sleep(1.2)

img2 = pyautogui.screenshot()
arr2 = np.array(img2)
r, g, b = arr2[450, 700, :3]
alive = r > 240 and g > 240 and b > 240
print(f"Dialog alive: {alive}")

# Check for new content (dropdown items) between y=420-540
print("Scanning for new content after gear click (y=420-540):")
for sy in range(420, 540, 5):
    row = arr2[sy, 220:510, :]
    avg = row.mean()
    if avg < 235:
        print(f"  y={sy}: avg brightness={avg:.1f} (DARK - possible dropdown item)")

# Save zoomed view of area below gear
zoom2 = img2.crop((215, 390, 520, 620))
draw = ImageDraw.Draw(zoom2)
for x in range(0, zoom2.width, 10):
    col = 'red' if x % 50 == 0 else 'pink'
    draw.line([(x,0),(x,zoom2.height)], fill=col, width=1)
    if x % 20 == 0:
        draw.text((x+1,1), str(x+215), fill='red')
for y in range(0, zoom2.height, 10):
    col = 'red' if y % 50 == 0 else 'pink'
    draw.line([(0,y),(zoom2.width,y)], fill=col, width=1)
    if y % 20 == 0:
        draw.text((1,y+1), str(y+390), fill='blue')
zoom2.resize((zoom2.width*3, zoom2.height*3)).save(
    r'C:\claude\personal-website\screenshots\after_gear_click_zoom.png')
print("Saved after_gear_click_zoom.png")
