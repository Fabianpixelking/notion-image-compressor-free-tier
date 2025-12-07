@echo off
echo.
echo ========================================================
echo       Notion Image Compressor - Folder Cleanup
echo ========================================================
echo.
echo This will delete ALL files in:
echo   - input\
echo   - output\
echo.
set /p confirm="Are you sure you want to continue? (y/n): "

if /i "%confirm%" neq "y" (
    echo.
    echo Operation cancelled.
    pause
    exit /b
)

:: Go up one level to root
cd ..

echo.
echo Clearing input folder...
pushd input
del /q *.*
echo. 2> .gitkeep
popd

echo Clearing output folder...
pushd output
del /q *.*
echo. 2> .gitkeep
popd

echo.
echo Done! Folders are clean.
pause
