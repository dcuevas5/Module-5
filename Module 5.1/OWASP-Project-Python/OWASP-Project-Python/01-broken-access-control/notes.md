Broken Access Control - Add auth and authorization checks. OWASP: https://owasp.org/www-project-top-ten/

# 01 — Broken Access Control

## Vulnerability
The original endpoint returned user data based only on a `user_id` URL parameter with **no authentication or authorization checks**. This allows anyone to read other users' data simply by changing the URL (Broken Access Control).

## How to reproduce (vulnerable)
1. Run the vulnerable app:
```bash
python 01-broken-access-control/vulnerable.py
