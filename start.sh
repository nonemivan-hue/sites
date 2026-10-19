#!/bin/bash

# Скрипт запуска TorrentFinder на адресе 192.168.110.77

echo "=========================================="
echo "  TorrentFinder - Поиск торрентов"
echo "=========================================="
echo ""

# Проверка Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 не найден. Установите Python 3.8 или выше."
    exit 1
fi

# Установка Flask если не установлен
echo "📦 Проверка зависимостей..."
python3 -m pip install flask --quiet

# Запуск приложения
echo ""
echo "🚀 Запуск сервера..."
echo "📍 Адрес: http://192.168.110.77:5000"
echo "🛑 Для остановки нажмите Ctrl+C"
echo ""

python3 app.py
