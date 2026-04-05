# Day 4 Report — Labs 6–7 (Docker + Jenkins + Security + Ansible)

## 1) Student
- **Name:** Karabaev Alikhan
- **Group:** IB-23-5b
- **Token:** D1-IB-23-5b-09-F0C3

## 2) Evidence checklist (files exist)
### Docker (6.2.7)
- artifacts/day4/docker/sampleapp_curl.txt: [Exists]
- artifacts/day4/docker/sampleapp_token_proof.txt: [Exists]
- artifacts/day4/docker/sampleapp_docker_ps.txt: [Exists]

### Jenkins (6.3.6)
- artifacts/day4/jenkins/pipeline_console.txt: [Exists]
- artifacts/day4/jenkins/pipeline_script.groovy: [Exists]

### Ansible (7.4.8)
- artifacts/day4/ansible/ansible_playbook_install.txt: [Exists]
- artifacts/day4/ansible/ports_conf_after.txt: [Exists]

### Security (6.5.10)
- artifacts/day4/security/db_tables.txt: [Exists]
- artifacts/day4/security/db_user_hash_sample.txt: [Exists]

## 3) Commands output
```text
python3 src/day4_summary_builder.py
pytest -q tests/test_day4_labs.py
# Result: 1 passed
```

## 4) Problems & fixes
- **Problem:** docker build failed with RuntimeError: can't start new thread.
- **Fix:** Added --progress-bar off to the pip install command in Dockerfile.
