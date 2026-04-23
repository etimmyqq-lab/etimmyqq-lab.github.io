@echo off
chcp 65001 >nul
echo ============================================
echo   一鍵發文（含審核 gate + 自動發社群）
echo ============================================
echo.

cd /d C:\claude\auto-post

echo [1] 呼叫 Claude 產內容 + 更新網站...
echo.
venv\Scripts\python.exe -m exposure.daily_pipeline %*
if %errorlevel% neq 0 (
    echo.
    echo [ERR] 產內容失敗，終止。
    pause
    exit /b 1
)

echo.
echo ============================================
echo   審核 gate
echo ============================================
echo.

:: 自動開啟 outbox 資料夾（讓你看產出的文字）
set TODAY=%DATE:~0,4%-%DATE:~5,2%-%DATE:~8,2%
if exist "C:\claude\personal-website\outbox\%TODAY%" (
    start "" "C:\claude\personal-website\outbox\%TODAY%"
)

:: 自動開啟首頁預覽
start "" http://127.0.0.1:8080/

echo.
echo 請審核：
echo   1. outbox 資料夾已開啟（linkedin.txt / threads.txt / youtube.txt）
echo   2. 網站首頁已開啟（看新文章卡片）
echo.
echo ============================================
echo 選項：
echo   y = 發佈網站 + 自動發 LinkedIn + 自動發 Threads 串文首則
echo   w = 只發佈網站（LinkedIn/Threads 手動貼）
echo   n = 都不發
echo ============================================
set /p APPROVE="請選擇 (y/w/n) "

if /i "%APPROVE%"=="n" (
    echo.
    echo [SKIP] 什麼都沒發。outbox 內容仍可手動使用。
    pause
    exit /b 0
)

:: 發佈網站（y 或 w 都會跑）
echo.
echo [2] 發佈網站到 GitHub Pages...
cd /d C:\claude\personal-website
if not exist ".git" (
    echo [!] 尚未 git 初始化，請先雙擊 deploy.bat。
    pause
    exit /b 1
)
git add .
git commit -m "publish article: %TODAY%"
git push
echo    -> 網站 1-2 分鐘後更新

:: 只有 y 才自動發社群
if /i "%APPROVE%"=="y" (
    echo.
    echo [3] 自動發 LinkedIn / Threads（Playwright 擬人化）...
    echo     視窗會彈出做操作，請勿關閉。
    cd /d C:\claude\auto-post
    venv\Scripts\python.exe -c "import asyncio, sys; sys.path.insert(0, '.'); from exposure.daily_pipeline import publish_to_social; from exposure import _common; from exposure.content_fanout import list_drafts, get_draft; drafts = list_drafts(); latest = get_draft(drafts[0]['id']) if drafts else None; print(asyncio.run(publish_to_social(latest['outputs'], headless=False)) if latest else 'no drafts')"
)

echo.
echo [DONE] 完成！
echo   - YouTube Shorts 腳本請查看 outbox/%TODAY%/youtube.txt（需實錄影片）
echo.
pause
