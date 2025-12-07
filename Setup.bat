@echo off
echo Setting up Notion Image Compressor...
powershell -ExecutionPolicy Bypass -File src/create_shortcuts.ps1
echo.
echo Setup complete! You can now use the 'Start' and 'Clear' shortcuts.
pause
