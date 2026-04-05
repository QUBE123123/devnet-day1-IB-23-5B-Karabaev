# Day 2 Report — Git + Data Formats + Tests

## 1) Student
- Name: Karabaev Alikhan
- Group: IB-23-5b
- Token: D1-IB-23-5b-09-F0C3
- Repo: https://github.com/QUBE123123/devnet-day1-IB-23-5b-karabaev
- PR link (day2): https://github.com/QUBE123123/devnet-day1-IB-23-5b-karabaev/pull/1

## 2) NetAcad progress
- Module 2.2 done: Yes + [Скриншот]
- Module 3.1–3.6 done: Python basics, Data Formats + [Скриншот]

## 3) Git evidence
- File `artifacts/day2/git_log.txt` exists: Yes
- File `artifacts/day2/conflict_log.txt` exists: Yes
- Conflict note: Conflicted on README.md while merging day2 branch. Resolved manually by choosing both changes.

## 4) Generated artifacts (Day2)
- normalized.json: Yes
- normalized.yaml: Yes
- normalized.xml: Yes
- normalized.csv: Yes
- summary.json: Yes

## 5) Commands output (paste EXACT output)
### 5.1 Generator
```text
Parsing artifacts/day1/response.json...
Exporting to JSON, YAML, XML, CSV...
Success! Files saved in artifacts/day2/parsing/
```
### 5.2 Tests
```text
.                                                                        [100%]
1 passed in 0.08s
```

## 6) What I learned
- Сравнение иерархических форматов данных (JSON vs XML vs YAML).
- Использование библиотек xmltodict и pyyaml для парсинга.
- Работа с Git ветками и разрешение конфликтов слияния (Merge Conflicts).

## 7) Problems & fixes
Problem: XML parser failed due to missing root element in dictionary.
Fix: Added a manual "root" wrapper to the dictionary before converting to XML.
Proof: artifacts/day2/parsing/books.xml exists and is valid.
