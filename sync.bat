@echo off
chcp 65001 >nul
echo ============================================
echo   個人網站 ^<- brand_profile.json 同步
echo ============================================
echo.

cd /d C:\claude\personal-website

if not exist "C:\claude\auto-post\venv\Scripts\python.exe" (
    echo [ERR] 找不到 auto-post 虛擬環境 Python
    pause
    exit /b 1
)

echo [1/2] 預覽會改什麼...
C:\claude\auto-post\venv\Scripts\python.exe sync_from_brand_profile.py --dry-run
echo.

set /p CONFIRM="是否要實際寫入？(y/n) "
if /i not "%CONFIRM%"=="y" (
    echo 取消。
    pause
    exit /b 0
)

echo.
echo [2/2] 正在同步...
C:\claude\auto-post\venv\Scripts\python.exe sync_from_brand_profile.py
echo.
echo [完成] 打開 http://127.0.0.1:8080/ 重新整理即可看到變更。
pause
