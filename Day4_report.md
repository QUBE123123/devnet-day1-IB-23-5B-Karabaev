# Day 4 Report — Docker, Jenkins, Ansible & Security Evolution

## 1) Student Info
- **Name:** Karabaev Alikhan
- **Group:** IB-23-5b
- **Token:** D1-IB-23-5b-09-F0C3
- **Repo:** https://github.com/QUBE123123/devnet-day1-IB-23-5b-karabaev

## 2) Timing (270 min)
- 0–60: Контейнеризация Flask-приложения с уникальным токеном f0c3a881.
- 60–120: Настройка Jenkins CI/CD Pipeline в Docker.
- 120–180: Автоматизация развертывания Apache через Ansible Playbooks.
- 180–270: Лабораторная по безопасности: миграция с Plain-text на Hashed passwords.

## 3) Evidence checklist
- artifacts/day4/docker/sampleapp_curl.txt: [Хэш f0c3a881 найден]
- artifacts/day4/jenkins/pipeline_console.txt: [Стадии Build/Test пройдены]
- artifacts/day4/ansible/ports_conf_after.txt: [Listen 8081 подтвержден]
- artifacts/day4/security/db_user_hash_sample.txt: [BCrypt хэш проверен]

## 4) Commands output
```text
python3 src/day4_summary_builder.py
pytest -q tests/test_day4_labs.py
# Result: 1 passed
```

## 5) Проблемы и решения
- **Проблема:** Docker-билд падал с ошибкой "can't start new thread" в виртуальной среде.
- **Решение:** Использовал базовый образ python:3.8-slim и отключил визуальный прогресс-бар pip через переменную окружения.

## 6) Рефлексия
Интеграция Docker и Jenkins показывает мощь современного подхода DevOps. Автоматизация настройки порта через Ansible исключает человеческий фактор при конфигурации серверов.
