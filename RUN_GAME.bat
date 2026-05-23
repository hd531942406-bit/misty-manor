@echo off
echo Starting Misty Manor...
echo.

if exist "C:\Users\Administrator\AppData\Local\Microsoft\WinGet\Packages\RenPy.RenPySDK_Microsoft.Winget.Source_8wekyb3d8bbwe\renpy-8.3.7-sdk\renpy.exe" (
    "C:\Users\Administrator\AppData\Local\Microsoft\WinGet\Packages\RenPy.RenPySDK_Microsoft.Winget.Source_8wekyb3d8bbwe\renpy-8.3.7-sdk\renpy.exe" "D:\MistyManor"
) else (
    echo Ren'Py SDK not found!
    echo Expected: C:\Users\Administrator\AppData\Local\Microsoft\WinGet\Packages\RenPy.RenPySDK_Microsoft.Winget.Source_8wekyb3d8bbwe\renpy-8.3.7-sdk\renpy.exe
)

echo.
echo Game closed. If there was an error, check traceback.txt in D:\MistyManor
pause
