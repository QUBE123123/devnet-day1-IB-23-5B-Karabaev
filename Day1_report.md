# Day 1 Report — Environment Setup & Hello API

## 1) Student
- **Name:** Karabaev Alikhan
- **Group:** IB-23-5b
- **Token:** D1-IB-23-5b-09-F0C3
- **Repo:** https://github.com/QUBE123123/devnet-day1-IB-23-5b-karabaev

## 2) Timing (270 min)
- 0–60: Установка Ubuntu/VM и настройка Python Venv
- 60–120: Конфигурация Git/GitHub и SSH ключей
- 120–180: Работа с REST API (Hello DevNet)
- 180–270: Документация и первый запуск Pytest

## 3) Evidence checklist
- artifacts/day1/environment_setup.json: [Есть]
- artifacts/day1/pip_freeze.txt: [Есть]
- src/day1_api_hello.py: [Есть]

## 4) Commands output
```text
python3 src/day1_api_hello.py
# Output: Hello DevNet! Student: Karabaev Alikhan, Group: IB-23-5b
pytest -q tests/test_day1_api_hello.py
# Result: 1 passed
```

## 5) Проблемы и решения
- **Проблема:** Ошибка аутентификации при первом push в GitHub.
- **Решение:** Перешел с использования пароля на Personal Access Token (PAT).
