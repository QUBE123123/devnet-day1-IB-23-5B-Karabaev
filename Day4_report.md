# Day 4 Report — Labs 6–7 (Docker + Jenkins + Security + Ansible)

## 1) Student
- **Name:** Karabaev Alikhan
- **Group:** IB-23-5b
- **Token:** D1-IB-23-5b-09-F0C3

## 2) Evidence checklist (files exist)
### Docker (6.2.7)
- artifacts/day4/docker/sampleapp_curl.txt: [Хэш f0c3a881 подтвержден]
- artifacts/day4/docker/sampleapp_token_proof.txt: [Найден]
- artifacts/day4/docker/sampleapp_docker_ps.txt: [Контейнер запущен]

### Jenkins (6.3.6)
- artifacts/day4/jenkins/pipeline_script.groovy: [Скрипт сохранен]
- artifacts/day4/jenkins/pipeline_console.txt: [Этапы: Preparation, Build, Results пройдены]

### Ansible (7.4.8)
- artifacts/day4/ansible/ansible_playbook_install.txt: [Лог установки Apache]
- artifacts/day4/ansible/ports_conf_after.txt: [Порт 8081 подтвержден]

### Security (6.5.10)
- artifacts/day4/security/db_tables.txt: [Таблица USER_HASH найдена]
- artifacts/day4/security/db_user_hash_sample.txt: [Пример хэшированного пароля]

## 3) Commands output
```text
python3 src/day4_summary_builder.py
pytest -q tests/test_day4_labs.py
# Result: 1 passed
```

## 4) Проблемы и решения
- **Проблема:** Ошибка "can't start new thread" при сборке Docker-образа.
- **Решение:** Использовал образ python:3.8-slim и отключил прогресс-бар pip.
