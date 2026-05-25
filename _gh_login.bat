@echo off
title GitHub CLI login
echo.
echo === GitHub CLI login (etimmyqq-lab) ===
echo.
echo Answer the prompts as follows:
echo   1. What account                : GitHub.com
echo   2. Preferred protocol          : HTTPS
echo   3. Authenticate Git            : Y
echo   4. How would you like to login : Login with a web browser
echo.
echo A one-time code will appear and the browser will open.
echo Sign in with the etimmyqq-lab account, then paste the code.
echo.
pause

"C:\Users\etimm\gh_portable\bin\gh.exe" auth login

echo.
echo === Done. You can close this window. ===
pause
