# OWASP-Project-Python
Project for demonstrating and fixing the OWASP Top 10 vulnerabilities in Python.

Structure:
- 01-broken-access-control
- 02-cryptographic-failures
- 03-sql-injection
- 04-nosql-injection
- 05-insecure-design
- 06-software-data-integrity
- 07-ssrf
- 08-identification-authentication
- 09-configuration-and-headers
- 10-logging-and-monitoring

Each folder contains:
- vulnerable.py  -- minimal vulnerable example
- fixed.py       -- corrected secure example
- notes.md       -- explanation + references (OWASP)

Instructions:
1. Create a Python venv and activate it.
2. `pip install -r requirements.txt`
3. Run examples: `python <folder>/vulnerable.py` or `python <folder>/fixed.py`

References:
- OWASP Top Ten: https://owasp.org/www-project-top-ten/
