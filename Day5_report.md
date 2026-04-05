# Day 5 Report — Module 8 Capstone (YANG + Webex + PT)

## 1) Student
- **Name:** Karabaev Alikhan
- **Token Hash:** f0c3a881

## 2) Evidence checklist
### YANG (8.3.5)
- artifacts/day5/yang/ietf-interfaces.yang: [Exists]
- artifacts/day5/yang/pyang_tree.txt: [Exists]

### Webex (8.6.7)
- artifacts/day5/webex/room_create.json: [Exists]
- artifacts/day5/webex/message_post.json: [Exists]

### Packet Tracer (8.8.3)
- artifacts/day5/pt/serviceTicket.txt: [Exists]
- artifacts/day5/pt/network_devices.json: [Exists]

## 3) Commands output
```text
python3 src/day5_summary_builder.py
pytest -q tests/test_day5_module8.py
# Result: 1 passed
```

## 4) Short reflection
The hardest part was managing the Webex Token expiration and ensuring the PT Controller external access was enabled.
