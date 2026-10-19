#!/bin/bash

# Скрипт проверки сетевого адреса

echo "=========================================="
echo "  Проверка сетевого адреса"
echo "=========================================="
echo ""

# Получение IP-адресов
echo "📍 Ваши IP-адреса:"
echo ""

if command -v ip &> /dev/null; then
    ip addr show | grep "inet " | grep -v "127.0.0.1" | awk '{print "  - " $2}' | cut -d'/' -f1
elif command -v ifconfig &> /dev/null; then
    ifconfig | grep "inet " | grep -v "127.0.0.1" | awk '{print "  - " $2}'
fi

echo ""
echo "=========================================="
echo ""

# Проверка целевого IP
TARGET_IP="192.168.110.77"

if command -v ip &> /dev/null; then
    if ip addr show | grep -q "$TARGET_IP"; then
        echo "✅ IP-адрес $TARGET_IP найден на этом компьютере"
        echo ""
        echo "🚀 Можете запускать приложение:"
        echo "   ./start.sh"
        echo ""
        echo "📍 Приложение будет доступно по адресу:"
        echo "   http://$TARGET_IP:5000"
    else
        echo "❌ IP-адрес $TARGET_IP НЕ найден на этом компьютере"
        echo ""
        echo "💡 Варианты решения:"
        echo "   1. Запустите скрипт на компьютере с IP $TARGET_IP"
        echo "   2. Измените IP в файле app.py на ваш текущий IP"
        echo "   3. Настройте статический IP $TARGET_IP на этом компьютере"
    fi
elif command -v ifconfig &> /dev/null; then
    if ifconfig | grep -q "$TARGET_IP"; then
        echo "✅ IP-адрес $TARGET_IP найден на этом компьютере"
        echo ""
        echo "🚀 Можете запускать приложение:"
        echo "   ./start.sh"
        echo ""
        echo "📍 Приложение будет доступно по адресу:"
        echo "   http://$TARGET_IP:5000"
    else
        echo "❌ IP-адрес $TARGET_IP НЕ найден на этом компьютере"
        echo ""
        echo "💡 Варианты решения:"
        echo "   1. Запустите скрипт на компьютере с IP $TARGET_IP"
        echo "   2. Измените IP в файле app.py на ваш текущий IP"
        echo "   3. Настройте статический IP $TARGET_IP на этом компьютере"
    fi
fi

echo ""
echo "=========================================="
