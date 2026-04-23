@echo off
chcp 65001 >nul
echo ============================================
echo   個人網站部署到 GitHub Pages
echo ============================================
echo.

cd /d C:\claude\personal-website

:: 檢查 git 是否已初始化
if not exist ".git" (
    echo [!] 這個目錄還沒 git 初始化。
    echo.
    echo 請先在瀏覽器做這些事：
    echo   1. 到 https://github.com/ 登入
    echo   2. 建立新 repo，名稱用：^<你的username^>.github.io
    echo   3. 不要勾選 "Initialize with README"（保持全空）
    echo   4. 複製 repo 的 HTTPS URL（形如 https://github.com/xxx/xxx.github.io.git^)
    echo.
    set /p REPO_URL="貼上 repo URL: "
    if "%REPO_URL%"=="" (
        echo 取消。
        pause
        exit /b 1
    )
    git init
    git branch -M main
    git remote add origin "%REPO_URL%"
    echo.
    echo [1] Git 已初始化。
)

:: 顯示變更
echo.
echo [2] 目前變更：
git status --short
echo.

set /p CONFIRM="是否要 commit + push？(y/n) "
if /i not "%CONFIRM%"=="y" (
    echo 取消。
    pause
    exit /b 0
)

:: Commit message
set /p MSG="Commit message（直接 Enter 用預設）: "
if "%MSG%"=="" set MSG=update personal website

echo.
echo [3] Commit 中...
git add .
git commit -m "%MSG%"

echo.
echo [4] Push 中...
git push -u origin main

echo.
echo [完成] 1-2 分鐘後到 https://^<你的username^>.github.io/ 看結果。
echo 首次部署記得到 Settings -^> Pages -^> Source 選 main branch + Save。
pause
