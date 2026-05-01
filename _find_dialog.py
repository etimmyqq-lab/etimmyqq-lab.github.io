# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import win32gui, win32con, win32api
import ctypes
import time
import pyautogui

# Check DPI awareness and actual click coordinate system
try:
    awareness = ctypes.c_int()
    ctypes.windll.shcore.GetProcessDpiAwareness(0, ctypes.byref(awareness))
    print(f"DPI Awareness: {awareness.value}")
except:
    print("Could not get DPI awareness")

# Get DPI scaling
dc = win32gui.GetDC(0)
dpi_x = win32api.GetDeviceCaps(dc, 88)  # LOGPIXELSX
win32gui.ReleaseDC(0, dc)
print(f"DPI: {dpi_x} (scale: {dpi_x/96*100:.0f}%)")

# pyautogui screen size
sz = pyautogui.size()
print(f"pyautogui size: {sz}")

# Find Edge window
EDGE_HWND = 0x1509c0
rect = win32gui.GetWindowRect(EDGE_HWND)
print(f"Edge window rect (logical): {rect}")

# Get actual mouse position to calibrate
import time
print("\nMove mouse to browser title bar area in 3 seconds...")
time.sleep(3)
pos = pyautogui.position()
print(f"Mouse position (pyautogui): {pos}")

# Get cursor pos via win32
import ctypes
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]
pt = POINT()
ctypes.windll.user32.GetCursorPos(ctypes.byref(pt))
print(f"Cursor position (win32): ({pt.x}, {pt.y})")
