@echo off
chcp 65001 >nul
echo ==========================================
echo   TorrentFinder - Поиск торрентов
echo ==========================================
echo.

REM Проверка Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python не найден. Установите Python 3.8 или выше.
    pause
    exit /b 1
)

REM Установка Flask
echo 📦 Проверка зависимостей...
python -m pip install flask --quiet

REM Запуск приложения
echo.
echo 🚀 Запуск сервера...
echo 📍 Адрес: http://192.168.110.77:5000
echo 🛑 Для остановки нажмите Ctrl+C
echo.

python app.py
pause
