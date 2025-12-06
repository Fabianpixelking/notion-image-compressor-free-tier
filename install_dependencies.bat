@echo off
echo Installing dependencies...
pip install Pillow imageio-ffmpeg
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Error installing Pillow. Please make sure Python is installed and added to PATH.
    pause
    exit /b
)
echo.
echo Dependencies installed successfully!
pause
