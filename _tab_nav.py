# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import win32gui, win32con
import time
import pyautogui
from PIL import Image

pyautogui.PAUSE = 0.2
EDGE_HWND = 0x1509c0

win32gui.ShowWindow(EDGE_HWND, win32con.SW_RESTORE)
win32gui.SetForegroundWindow(EDGE_HWND)
time.sleep(0.4)

# Click center of the dialog to focus it, then Tab through elements
# Dialog center is approximately screen (700, 700)
print("Clicking dialog center (700, 700)...")
pyautogui.click(700, 700)
time.sleep(0.4)

# Tab through UI elements; press Tab 3 times and try Enter/Space on the type dropdown
for i in range(4):
    pyautogui.press('tab')
    time.sleep(0.3)

# At this point we might be on "選取類型" - try pressing Enter and Down
pyautogui.press('enter')
time.sleep(1.0)

img = pyautogui.screenshot()
popup = img.crop((200, 380, 1400, 1100))
popup.resize((popup.width//2, popup.height//2)).save(
    r'C:\claude\personal-website\screenshots\after_tab_enter.png')
print("Saved")
