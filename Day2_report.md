# Day 2 Report — Data Formats & RESTCONF

## 1) Student Info
- **Name:** Karabaev Alikhan
- **Group:** IB-23-5b
- **Token:** D1-IB-23-5b-09-F0C3
- **Repo:** https://github.com/QUBE123123/devnet-day1-IB-23-5b-karabaev

## 2) Timing (270 min)
- 0–90: Анализ структур JSON, XML и YAML. Сравнение иерархий.
- 90–180: Написание универсального парсера в src/day2_data_formats.py.
- 180–240: Изучение RESTCONF и структуры leaf-узлов.
- 240–270: Валидация всех форматов через автоматические тесты.

## 3) Evidence checklist
- artifacts/day2/parsing/books.json: [Валидно]
- artifacts/day2/parsing/books.xml: [Валидно]
- artifacts/day2/parsing/books.yaml: [Валидно]

## 4) Commands output
```text
pytest -q tests/test_day2_data_formats.py
# Result: 1 passed
```

## 5) Проблемы и решения
- **Проблема:** Библиотека xmltodict генерировала структуру, которая не проходила валидацию по схеме.
- **Решение:** Добавил принудительную фильтрацию корневых элементов при конвертации из XML в JSON.

## 6) Рефлексия
Понимание того, как данные трансформируются между форматами, необходимо для работы с мульти-вендорным оборудованием, где одно устройство может отдавать XML, а другое JSON.
