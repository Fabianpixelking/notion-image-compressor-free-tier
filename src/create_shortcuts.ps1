$WshShell = New-Object -comObject WScript.Shell

# 1. Create Start Compressor Shortcut
$ShortcutPath = "$PSScriptRoot\..\Start Compressor.lnk"
$Target = "$PSScriptRoot\run.bat"
$Shortcut = $WshShell.CreateShortcut($ShortcutPath)
$Shortcut.TargetPath = $Target
$Shortcut.WorkingDirectory = "$PSScriptRoot"
# Use a System Icon (imageres.dll index 173 is a camera/picture icon often, or shell32.dll)
# shell32.dll index 305 is a camera
$Shortcut.IconLocation = "shell32.dll,305" 
$Shortcut.Description = "Start Notion Image Compressor"
$Shortcut.Save()
Write-Host "Created 'Start Compressor.lnk'"

# 2. Create Clear Folders Shortcut
$ShortcutPath = "$PSScriptRoot\..\Reset & Clear.lnk"
$Target = "$PSScriptRoot\clear.bat"
$Shortcut = $WshShell.CreateShortcut($ShortcutPath)
$Shortcut.TargetPath = $Target
$Shortcut.WorkingDirectory = "$PSScriptRoot"
# shell32.dll index 31 or 32 is trash can
$Shortcut.IconLocation = "shell32.dll,32" 
$Shortcut.Description = "Delete all files in input/output"
$Shortcut.Save()
Write-Host "Created 'Reset & Clear.lnk'"
