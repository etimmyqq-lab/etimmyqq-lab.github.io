# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import win32gui, win32con, win32clipboard
import time
import pyautogui

pyautogui.PAUSE = 0.15
EDGE_HWND = 0x1509c0

# Read the script file as UTF-8
with open(r'C:\claude\personal-website\intake-script.gs', 'r', encoding='utf-8') as f:
    code = f.read()

print(f"Read {len(code)} chars, {code.count(chr(10))+1} lines")

# Put into clipboard using win32clipboard with CF_UNICODETEXT (proper Unicode, no encoding loss)
win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, code)
win32clipboard.CloseClipboard()
print("Clipboard set with CF_UNICODETEXT")

# Bring Edge to front
win32gui.ShowWindow(EDGE_HWND, win32con.SW_RESTORE)
win32gui.SetForegroundWindow(EDGE_HWND)
time.sleep(0.5)

# Click into the Apps Script code editor area
print("Clicking editor at (750, 600)...")
pyautogui.click(750, 600)
time.sleep(0.4)

# Select all existing code and replace with new paste
pyautogui.hotkey('ctrl', 'a')
time.sleep(0.3)
pyautogui.hotkey('ctrl', 'v')
time.sleep(1.2)

# Save with Ctrl+S
pyautogui.hotkey('ctrl', 's')
time.sleep(2.0)

print("Done — pasted and saved")
title = win32gui.GetWindowText(EDGE_HWND)
print(f"Title: {title[:80]}")
