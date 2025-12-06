@echo off
echo Starting Image Compression Tool...
python compress_images.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo An error occurred!
) else (
    echo.
    echo Process completed successfully.
)
echo.
pause
