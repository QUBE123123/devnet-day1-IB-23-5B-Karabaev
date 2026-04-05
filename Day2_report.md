# Day 2 Report — Data Formats & Parsing

## 1) Student
- **Name:** Karabaev Alikhan
- **Group:** IB-23-5b

## 2) Timing (270 min)
- 0–90: Изучение структур XML, JSON, YAML
- 90–180: Написание скриптов кросс-парсинга (day2_data_formats.py)
- 180–270: Тестирование валидации через jsonschema

## 3) Evidence checklist
- artifacts/day2/parsing/books.json: [Есть]
- artifacts/day2/parsing/books.xml: [Есть]
- artifacts/day2/parsing/books.yaml: [Есть]

## 4) Commands output
```text
pytest -q tests/test_day2_data_formats.py
# Result: 1 passed
```

## 5) Проблемы и решения
- **Проблема:** Ошибка валидации XML из-за неправильного корневого тега.
- **Решение:** Исправил структуру в скрипте, добавив обязательный заголовок XML.
