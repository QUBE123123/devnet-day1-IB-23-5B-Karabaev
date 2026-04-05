# Day 3 Report — Lab 4.5.5 + Auto-check artifacts

## 1) Student
- Name: Karabaev Alikhan
- Group: IB-23-5b
- Token: D1-IB-23-5b-09-F0C3
- Repo: https://github.com/QUBE123123/devnet-day1-IB-23-5b-karabaev

## 2) Lab 4.5.5 completion evidence
- API docs screenshots: [API Explore]
- Postman screenshots: [Collection Run]
- Python run screenshot: [Script Output]

## 3) Artifacts checklist
- artifacts/day3/books_before.json: Yes
- artifacts/day3/books_sorted_isbn.json: Yes
- artifacts/day3/mybook_post.json: Yes
- artifacts/day3/books_by_me.json: Yes
- artifacts/day3/add100_report.json: Yes
- artifacts/day3/postman_collection.json: Yes
- artifacts/day3/postman_environment.json: Yes
- artifacts/day3/curl_get_books.txt: Yes
- artifacts/day3/curl_get_books_isbn.txt: Yes
- artifacts/day3/curl_get_books_sorted.txt: Yes
- artifacts/day3/summary.json: Yes

## 4) Command outputs (paste exact)
### 4.1 Script run
```text
Adding 100 books to library...
Progress: [####################] 100%
Report saved to artifacts/day3/add100_report.json
```
### 4.2 Tests
```text
.                                                                        [100%]
1 passed in 0.12s
```

## 5) Problems & fixes
Problem: Library API returned 401 Unauthorized for batch POST requests.
Fix: Corrected the Authorization header to use "Bearer" with the student token.
Proof: artifacts/day3/add100_report.json shows 100 success entries.
