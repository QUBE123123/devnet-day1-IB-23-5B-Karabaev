# Day 5 Report — Module 8 Capstone (YANG, Webex & SDN)

## 1) Student Info
- **Name:** Karabaev Alikhan
- **Group:** IB-23-5b
- **Token:** D1-IB-23-5b-09-F0C3
- **Repo:** https://github.com/QUBE123123/devnet-day1-IB-23-5b-karabaev

## 2) Timing (270 min)
- 0–60: Работа с моделями данных YANG (ietf-interfaces) и инструментом pyang.
- 60–150: Программирование облачного API Webex: создание комнат и отправка уведомлений.
- 150–240: REST API Packet Tracer Controller: авторизация по тикетам и сбор данных о хостах.
- 240–270: Финальная валидация всего Capstone-проекта.

## 3) Evidence checklist
- artifacts/day5/yang/pyang_tree.txt: [Дерево интерфейсов построено]
- artifacts/day5/webex/room_create.json: [Название содержит f0c3a881]
- artifacts/day5/pt/serviceTicket.txt: [X-Auth-Token получен]

## 4) Commands output
```text
python3 src/day5_summary_builder.py
pytest -q tests/test_day5_module8.py
# Result: 1 passed
```

## 5) Проблемы и решения
- **Проблема:** Webex-токен перестал работать через 12 часов после начала лабы.
- **Решение:** Обновил временный токен на портале разработчика и перенастроил переменную окружения WEBEX_TOKEN.

## 6) Рефлексия
Capstone проект объединил облачные технологии и управление локальной сетью. Это демонстрирует, как современный инженер может управлять инфраструктурой любого масштаба через API.
