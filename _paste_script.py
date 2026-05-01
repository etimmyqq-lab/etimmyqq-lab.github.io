"""Find the Chrome window with Apps Script open and paste the code."""
import win32gui
import win32con
import win32api
import win32clipboard
import time
import subprocess
import sys

def get_chrome_windows():
    windows = []
    def enum_cb(hwnd, extra):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)
            if title:
                windows.append((hwnd, title))
    win32gui.EnumWindows(enum_cb, None)
    return windows

def focus_and_paste(hwnd):
    # Bring window to front
    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
    win32gui.SetForegroundWindow(hwnd)
    time.sleep(0.8)

    # Click in the editor area (approximate center of window)
    rect = win32gui.GetWindowRect(hwnd)
    cx = (rect[0] + rect[2]) // 2
    cy = (rect[1] + rect[3]) // 2
    win32api.SetCursorPos((cx, cy))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, cx, cy, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, cx, cy, 0, 0)
    time.sleep(0.3)

    # Ctrl+A to select all
    win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)
    win32api.keybd_event(ord('A'), 0, 0, 0)
    win32api.keybd_event(ord('A'), 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.3)

    # Ctrl+V to paste
    win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)
    win32api.keybd_event(ord('V'), 0, 0, 0)
    win32api.keybd_event(ord('V'), 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.5)

    # Ctrl+S to save
    win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)
    win32api.keybd_event(ord('S'), 0, 0, 0)
    win32api.keybd_event(ord('S'), 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)
    print("Done: Ctrl+A, Ctrl+V, Ctrl+S sent")

# List all Chrome windows
windows = get_chrome_windows()
chrome_wins = [(h, t) for h, t in windows if 'Chrome' in t or 'Google' in t or 'Apps Script' in t or 'script' in t.lower()]

print("Chrome windows found:")
for i, (h, t) in enumerate(chrome_wins):
    safe = t.encode('ascii', errors='replace').decode('ascii')
    print(f"  [{i}] {safe}")

if not chrome_wins:
    print("No Chrome windows found")
    sys.exit(1)

# Find Apps Script window
target = None
for h, t in chrome_wins:
    if 'Apps Script' in t or 'script' in t.lower() or 'Script' in t:
        target = (h, t)
        break

if not target:
    target = chrome_wins[0]
    safe = target[1].encode('ascii', errors='replace').decode('ascii')
    print(f"Apps Script window not found, using: {safe}")
else:
    safe = target[1].encode('ascii', errors='replace').decode('ascii')
    print(f"Found Apps Script window: {safe}")

focus_and_paste(target[0])
