# Day 4 Report — Labs 6–7 (Docker + Jenkins + Security + Ansible)

## 1) Student
- Name: Karabaev Alikhan
- Group: IB-23-5b
- Token: D1-IB-23-5b-09-F0C3
- Repo: https://github.com/QUBE123123/devnet-day1-IB-23-5b-karabaev

## 2) Evidence checklist (files exist)
### Docker (6.2.7)
- artifacts/day4/docker/sampleapp_curl.txt: Yes
- artifacts/day4/docker/sampleapp_token_proof.txt: Yes
- artifacts/day4/docker/sampleapp_docker_ps.txt: Yes
- artifacts/day4/docker/sampleapp_build_log.txt: Yes

### Jenkins (6.3.6)
- artifacts/day4/jenkins/jenkins_docker_ps.txt: Yes
- artifacts/day4/jenkins/buildapp_console.txt: Yes
- artifacts/day4/jenkins/testapp_console.txt: Yes
- artifacts/day4/jenkins/pipeline_script.groovy: Yes
- artifacts/day4/jenkins/pipeline_console.txt: Yes
- artifacts/day4/jenkins/jenkins_url.txt: Yes

### Ansible (7.4.8)
- artifacts/day4/ansible/ansible_ping.txt: Yes
- artifacts/day4/ansible/ansible_hello.txt: Yes
- artifacts/day4/ansible/ansible_playbook_install.txt: Yes
- artifacts/day4/ansible/ports_conf_after.txt: Yes
- artifacts/day4/ansible/curl_apache_8081.txt: Yes

### Security (6.5.10)
- artifacts/day4/security/signup_v1.txt: Yes
- artifacts/day4/security/login_v1.txt: Yes
- artifacts/day4/security/signup_v2.txt: Yes
- artifacts/day4/security/login_v2.txt: Yes
- artifacts/day4/security/db_tables.txt: Yes
- artifacts/day4/security/db_user_hash_sample.txt: Yes

## 3) Commands output
```text
Summary generated for token_hash8: f0c3a881
Validation Passed: True
.                                                                        [100%]
1 passed in 0.15s
```

## 4) Short reflection
Самым сложным сегодня была отладка Jenkins Pipeline внутри Docker-контейнера. Нужно было правильно пробросить порты и дождаться инициализации. Ошибка безопасности, которую я исправил: миграция с хранения паролей в открытом виде на использование хэшей (bcrypt). Это предотвращает утечку учетных данных при компрометации базы данных.

## 5) Problems & fixes
Problem: Docker build error "can't start new thread" due to VM resource limits.
Fix: Used "python:3.8-slim" base image and disabled pip progress bars to save memory.
Proof: artifacts/day4/docker/sampleapp_build_log.txt (Successful build).
