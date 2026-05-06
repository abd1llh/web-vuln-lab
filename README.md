# 🔐 Web Vulnerability Lab

A hands-on cybersecurity project demonstrating SQL Injection attack and defense.

## What this project does
- Built a login system vulnerable to SQL Injection
- Demonstrated how an attacker can bypass authentication
- Fixed the vulnerability using parameterized queries

## Technologies
- Python
- Flask
- SQLite

## How to run
pip install flask
python app.py

## Vulnerability Demo
**Attack:** `admin' OR '1'='1' --` bypasses login without a password  
**Fix:** Parameterized queries prevent SQL injection

## Author
abd1llh | abd1llh.online
