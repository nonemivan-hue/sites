@echo off
chcp 65001 >nul
echo ==========================================
echo   Проверка сетевого адреса
echo ==========================================
echo.

echo 📍 Ваши IP-адреса:
echo.
ipconfig | findstr /i "IPv4"
echo.
echo ==========================================
echo.

set TARGET_IP=192.168.110.77

ipconfig | findstr /i "%TARGET_IP%" >nul
if %errorlevel% equ 0 (
    echo ✅ IP-адрес %TARGET_IP% найден на этом компьютере
    echo.
    echo 🚀 Можете запускать приложение:
    echo    start.bat
    echo.
    echo 📍 Приложение будет доступно по адресу:
    echo    http://%TARGET_IP%:5000
) else (
    echo ❌ IP-адрес %TARGET_IP% НЕ найден на этом компьютере
    echo.
    echo 💡 Варианты решения:
    echo    1. Запустите скрипт на компьютере с IP %TARGET_IP%
    echo    2. Измените IP в файле app.py на ваш текущий IP
    echo    3. Настройте статический IP %TARGET_IP% на этом компьютере
)

echo.
echo ==========================================
pause
