import pyautogui, win32gui
import sys
sys.stdout.reconfigure(encoding='utf-8')
EDGE_HWND = 0x1509c0
win32gui.ShowWindow(EDGE_HWND, 9)
win32gui.SetForegroundWindow(EDGE_HWND)
import time; time.sleep(0.5)
img = pyautogui.screenshot()
img.save(r'C:\claude\personal-website\screenshots\now.png')
print(win32gui.GetWindowText(EDGE_HWND)[:80])
