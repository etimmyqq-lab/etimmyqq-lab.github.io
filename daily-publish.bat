@echo off
chcp 65001 >nul
echo ============================================
echo   一鍵發文（含審核 gate）
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

:: 自動開啟 outbox 資料夾（讓你看 3 平台文字）
set TODAY=%DATE:~0,4%-%DATE:~5,2%-%DATE:~8,2%
if exist "C:\claude\personal-website\outbox\%TODAY%" (
    start "" "C:\claude\personal-website\outbox\%TODAY%"
)

:: 自動開啟首頁（讓你看新文章卡片 + 文章頁）
start "" http://127.0.0.1:8080/

echo.
echo 請審核：
echo   1. outbox 資料夾已開啟（linkedin.txt / threads.txt / youtube.txt）
echo   2. 網站首頁已開啟（看新文章卡片）
echo   3. 點擊卡片進入文章頁確認長文 OK
echo.
echo 三份社群內容請直接複製貼到 LinkedIn / Threads / YouTube。
echo.
set /p APPROVE="文章 OK 要發佈網站嗎？(y/n/e=編輯後再發) "

if /i "%APPROVE%"=="e" (
    echo.
    echo 請手動編輯檔案後再跑 deploy.bat
    pause
    exit /b 0
)

if /i not "%APPROVE%"=="y" (
    echo.
    echo [SKIP] 未發佈網站。outbox 的 3 份社群文字仍可使用。
    pause
    exit /b 0
)

echo.
echo [2] 發佈網站到 GitHub Pages...
echo.
cd /d C:\claude\personal-website

if not exist ".git" (
    echo [!] 尚未 git 初始化，請先雙擊 deploy.bat 設定 repo。
    pause
    exit /b 1
)

git add .
git commit -m "publish article: %TODAY%"
git push

echo.
echo [DONE] 發佈完成！
echo   - 網站：1-2 分鐘後上線
echo   - outbox 內的 3 份文字請手動貼到 LinkedIn / Threads / YouTube
echo.
pause
