# -*- coding: utf-8 -*-
import win32gui
import sys

sys.stdout.reconfigure(encoding='utf-8')

windows = []
def cb(hwnd, _):
    if win32gui.IsWindowVisible(hwnd):
        t = win32gui.GetWindowText(hwnd)
        if t and len(t) > 2:
            windows.append((hwnd, t))
win32gui.EnumWindows(cb, None)

for h, t in windows:
    print(hex(h), t[:100])
