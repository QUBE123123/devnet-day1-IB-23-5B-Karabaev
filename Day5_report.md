# Day 5 Report — Module 8 Capstone (YANG + Webex + PT)

## 1) Student
- **Name:** Karabaev Alikhan
- **Token Hash:** f0c3a881

## 2) Evidence checklist
### YANG (8.3.5)
- artifacts/day5/yang/ietf-interfaces.yang: [Файл сохранен]
- artifacts/day5/yang/pyang_tree.txt: [Дерево сгенерировано]

### Webex (8.6.7)
- artifacts/day5/webex/room_create.json: [Комната DevNet-Capstone-f0c3a881]
- artifacts/day5/webex/message_post.json: [Сообщение отправлено]

### Packet Tracer (8.8.3)
- artifacts/day5/pt/serviceTicket.txt: [Тикет получен]
- artifacts/day5/pt/network_devices.json: [Данные устройств получены]

## 3) Commands output
```text
python3 src/day5_summary_builder.py
pytest -q tests/test_day5_module8.py
# Result: 1 passed
```

## 4) Проблемы и решения
- **Проблема:** Срок действия токена Webex истек во время тестов.
- **Решение:** Обновил токен на портале разработчика и переэкспортировал переменную окружения.
