# Day 3 Report — Library API & Postman Automation

## 1) Student Info
- **Name:** Karabaev Alikhan
- **Group:** IB-23-5b
- **Token:** D1-IB-23-5b-09-F0C3
- **Repo:** https://github.com/QUBE123123/devnet-day1-IB-23-5b-karabaev

## 2) Timing (270 min)
- 0–90: Работа с библиотекой Python Requests: GET и POST запросы к API.
- 90–180: Массовая автоматизация: создание скрипта для добавления 100 книг.
- 180–240: Работа в Postman: создание коллекции и настройка окружения (Environments).
- 240–270: Сборка итогового summary.json.

## 3) Evidence checklist
- artifacts/day3/summary.json: [Сформирован]
- artifacts/day3/postman_collection.json: [Экспортирован]
- artifacts/day3/add100_report.json: [95+ книг добавлено успешно]

## 4) Проблемы и решения
- **Проблема:** При массовой отправке запросов API иногда возвращало ошибку 401.
- **Решение:** Оптимизировал передачу заголовка Authorization, вынеся его в глобальную сессию requests.Session().

## 5) Рефлексия
Использование Postman вместе с Python позволяет быстро прототипировать запросы перед тем, как переносить их в полноценный код автоматизации.
