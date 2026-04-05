# Day 5 Report — Module 8 Capstone

## 1) Student
- Name: Karabaev Alikhan
- Group: IB-23-5b
- Token: D1-IB-23-5b-09-F0C3
- Repo: https://github.com/QUBE123123/devnet-day1-IB-23-5b-karabaev

## 2) YANG (8.3.5)
- Evidence files:
  - artifacts/day5/yang/ietf-interfaces.yang [Yes]
  - artifacts/day5/yang/pyang_version.txt [Yes]
  - artifacts/day5/yang/pyang_tree.txt [Yes]
- Screenshot: [Вставь скриншот pyang tree]

## 3) Webex (8.6.7)
- Room title contains token_hash8 (f0c3a881): Yes
- Message text contains token_hash8 (f0c3a881): Yes
- Evidence files:
  - me.json, rooms_list.json, room_create.json, message_post.json, messages_list.json [All Yes]

## 4) Packet Tracer Controller REST (8.8.3)
- external_access_check contains “empty ticket”: Yes
- serviceTicket saved: Yes
- Evidence files:
  - external_access_check.json, network_devices.json, hosts.json [Yes]
  - postman_collection.json, postman_environment.json [Yes]
  - pt_internal_output.txt [Yes]

## 5) Commands output (paste exact)
```text
Summary 5.0 generated. Webex/YANG/PT checks: OK.
.                                                                        [100%]
1 passed in 0.18s
```

## 6) Problems & fixes
Problem: Webex Personal Access Token expired (12h limit).
Fix: Refreshed the token on developer.webex.com and re-ran the script with the new WEBEX_TOKEN env variable.
Proof: artifacts/day5/webex/room_create.json (Status: 201 Created).
