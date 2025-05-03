@echo off
echo Running Port Scanner...
python "Port Scanner.py"
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] The script encountered an issue.
)
pause
