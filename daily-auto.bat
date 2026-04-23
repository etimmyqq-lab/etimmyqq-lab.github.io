@echo off
chcp 65001 >nul
:: ============================================
:: 每日全自動化（給 Windows Task Scheduler）
:: ============================================
:: 不顯示任何互動、無審核、headless 瀏覽器
::   1. 產內容（Claude 4 平台）
::   2. 更新網站 + 自動 git push
::   3. headless 自動發 LinkedIn + Threads（經 auto-post 既有 Playwright）
::   4. 所有輸出寫到 auto-post/logs/daily-auto.log
:: ============================================

set LOGFILE=C:\claude\auto-post\logs\daily-auto.log
if not exist "C:\claude\auto-post\logs\" mkdir "C:\claude\auto-post\logs\"

echo. >> "%LOGFILE%"
echo [%DATE% %TIME%] daily-auto start >> "%LOGFILE%"

:: Step 1 產內容 + 發社群（一次搞定）
cd /d C:\claude\auto-post
venv\Scripts\python.exe -m exposure.daily_pipeline --publish --headless >> "%LOGFILE%" 2>&1
if %errorlevel% neq 0 (
    echo [%DATE% %TIME%] daily_pipeline FAILED, aborting >> "%LOGFILE%"
    exit /b 1
)

:: Step 2 git push 網站
cd /d C:\claude\personal-website
if exist ".git" (
    set TODAY=%DATE:~0,4%-%DATE:~5,2%-%DATE:~8,2%
    git add . >> "%LOGFILE%" 2>&1
    git commit -m "auto-publish: %TODAY%" >> "%LOGFILE%" 2>&1
    git push >> "%LOGFILE%" 2>&1
    echo [%DATE% %TIME%] git push done >> "%LOGFILE%"
) else (
    echo [%DATE% %TIME%] .git missing, skip push >> "%LOGFILE%"
)

echo [%DATE% %TIME%] daily-auto END >> "%LOGFILE%"
exit /b 0
