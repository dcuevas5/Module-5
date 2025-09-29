# 03 â€” SQL Injection

## Vulnerability
The vulnerable example builds SQL queries by concatenating user input into a string. This allows an attacker to inject SQL operators (e.g., `' OR '1'='1`) and bypass intended filters.

## How to reproduce (vulnerable)
1. Run: `python 03-sql-injection/vulnerable.py`
2. Try: injection payloads and observe results.

## How to reproduce (fixed)
1. Run: `python 03-sql-injection/fixed.py`
2. The parameterized query prevents injection even with malicious input.

## Fix applied
- Use parameterized queries / prepared statements.

## References
- OWASP SQL Injection Prevention Cheat Sheet.
