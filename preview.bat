@echo off
chcp 65001 >nul
echo ============================================
echo   個人網站本地預覽
echo   http://127.0.0.1:8080/
echo ============================================
echo.
echo 按 Ctrl+C 停止預覽。
echo.

cd /d C:\claude\personal-website

:: 自動開啟瀏覽器
start "" http://127.0.0.1:8080/

:: 啟動 Python 內建 HTTP server
C:\claude\auto-post\venv\Scripts\python.exe -m http.server 8080
