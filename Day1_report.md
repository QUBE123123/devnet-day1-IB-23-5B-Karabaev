# Day 1 Report — Environment Setup & Hello API

## 1) Student Info
- **Name:** Karabaev Alikhan
- **Group:** IB-23-5b
- **Token:** D1-IB-23-5b-09-F0C3
- **Repo:** https://github.com/QUBE123123/devnet-day1-IB-23-5b-karabaev

## 2) Timing (270 min)
- 0–60: Установка и базовая настройка Ubuntu DEVASC VM.
- 60–120: Создание виртуального окружения Python и установка зависимостей.
- 120–210: Настройка Git: генерация SSH-ключей, создание PAT-токена и привязка удаленного репозитория.
- 210–270: Проверка API-связности и написание базового скрипта приветствия.

## 3) Evidence checklist
- artifacts/day1/environment_setup.json: [Подтверждено]
- artifacts/day1/pip_freeze.txt: [Подтверждено]
- src/day1_api_hello.py: [Код проверен]

## 4) Commands output
```text
python3 src/day1_api_hello.py
# Output: Hello DevNet! Student: Karabaev Alikhan, Group: IB-23-5b
pytest -q tests/test_day1_api_hello.py
# Result: 1 passed
```

## 5) Проблемы и решения
- **Проблема:** Git запрашивал пароль при каждом пуше, но обычный пароль от GitHub не принимался.
- **Решение:** Создал классический Personal Access Token (PAT) в настройках GitHub и использовал его вместо пароля.

## 6) Рефлексия
Первый день заложил фундамент. Работа с виртуальными окружениями Python позволяет избежать конфликтов библиотек, а правильная настройка Git критически важна для командной разработки.
