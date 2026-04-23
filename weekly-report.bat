@echo off
chcp 65001 >nul
echo ============================================
echo   週報 + AI 可見度監測
echo   ↓
echo   這會呼叫 Claude CLI 跑 6-12 次（2-3 分鐘）
echo ============================================
echo.

cd /d C:\claude\auto-post

venv\Scripts\python.exe -m exposure.weekly_report %*
if %errorlevel% neq 0 (
    echo.
    echo [ERR] 週報產出失敗。
    pause
    exit /b 1
)

:: 找最新的週報檔自動開啟
for /f "delims=" %%f in ('dir /b /o-d "C:\claude\auto-post\reports\*.md" 2^>nul') do (
    start "" "C:\claude\auto-post\reports\%%f"
    goto :done
)

:done
echo.
pause
