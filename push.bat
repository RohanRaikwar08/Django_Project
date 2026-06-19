@echo off
cd /d "%~dp0"

git add .

git diff --cached --quiet
if %errorlevel%==0 (
    echo No changes to commit.
    pause
    exit
)

set /p msg=Commit Message: 

git commit -m "%msg%"
git push

echo.
echo Push Successful!
pause