@echo off
pushd "%~dp0"

:: Check for Python
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Error: Python is not installed or not in PATH.
    echo Please install Python from https://www.python.org/downloads/
    echo WITHOUT Python, this tool cannot work.
    pause
    exit /b
)

:: Check/Install Dependencies
:: We check if imageio-ffmpeg is installed by trying to import it
python -c "import imageio_ffmpeg" >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo First run detected! Installing necessary components...
    echo This might take a minute.
    pip install Pillow imageio-ffmpeg
    if %ERRORLEVEL% NEQ 0 (
        echo.
        echo Error installing dependencies.
        pause
        exit /b
    )
    echo.
    echo Setup complete! Starting compressor...
    echo.
)

:: Run the compressor
python compress_media.py
pause
