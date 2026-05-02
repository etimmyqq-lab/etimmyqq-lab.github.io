# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import win32gui, win32con
import time
import pyautogui
import numpy as np
from PIL import Image, ImageDraw

pyautogui.PAUSE = 0.15
EDGE_HWND = 0x1509c0

win32gui.ShowWindow(EDGE_HWND, win32con.SW_RESTORE)
win32gui.SetForegroundWindow(EDGE_HWND)
time.sleep(0.4)

def check_alive():
    img = pyautogui.screenshot()
    arr = np.array(img)
    r, g, b = arr[450, 700, :3]
    return r > 240 and g > 240 and b > 240, img

# Step 1: Click in the left panel "選取類型" ROW but LEFT of gear (x≈280, y=470)
print("Clicking left of gear in 選取類型 row...")
pyautogui.click(280, 470)
time.sleep(0.3)

# Step 2: Tab once → should focus gear
print("Tab to focus gear...")
pyautogui.press('tab')
time.sleep(0.2)

# Step 3: Space to open dropdown
print("Space to open dropdown...")
pyautogui.press('space')
time.sleep(0.2)  # 200ms - quick check

# Step 4: Snapshot immediately to see dropdown
alive, img = check_alive()
arr = np.array(img)

# Look for dark content between y=480-530 (between gear bottom and API 執行檔)
found_items = []
for sy in range(480, 535):
    row = arr[sy, 225:510, :]
    avg = row.mean()
    if avg < 235:
        found_items.append((sy, avg))

print(f"Dialog alive: {alive}")
print(f"Dark content at y=480-535: {found_items[:10]}")

# Save zoomed view
zoom = img.crop((215, 460, 530, 600))
draw = ImageDraw.Draw(zoom)
for x in range(0, zoom.width, 20):
    draw.line([(x,0),(x,zoom.height)], fill='red', width=1)
    draw.text((x+1,1), str(x+215), fill='red')
for y in range(0, zoom.height, 10):
    draw.line([(0,y),(zoom.width,y)], fill='blue', width=1)
    draw.text((1,y+1), str(y+460), fill='blue')
zoom.resize((zoom.width*4, zoom.height*4)).save(
    r'C:\claude\personal-website\screenshots\dropdown_460.png')
print("Saved dropdown_460.png")

if found_items:
    # Dropdown items detected! Click first item
    item_y = found_items[0][0]
    print(f"\nDropdown item detected at y={item_y}! Clicking '網頁應用程式'...")
    pyautogui.click(350, item_y)
    time.sleep(1.0)
    alive2, img2 = check_alive()
    print(f"After item click, dialog alive: {alive2}")

    # Save result
    if alive2:
        full = img2.crop((215, 390, 1370, 800))
        draw = ImageDraw.Draw(full)
        for x in range(0, full.width, 100):
            draw.line([(x,0),(x,full.height)], fill='red', width=1)
            draw.text((x+2,2), str(x+215), fill='red')
        for y in range(0, full.height, 100):
            draw.line([(0,y),(full.width,y)], fill='red', width=1)
            draw.text((2,y+2), str(y+390), fill='red')
        full.resize((full.width//2, full.height//2)).save(
            r'C:\claude\personal-website\screenshots\final_type_selected.png')
        print("Saved final_type_selected.png")
