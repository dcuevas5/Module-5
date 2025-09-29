# 02 — Cryptographic Failures (Password Hashing)

## Vulnerability
The vulnerable example uses an insecure hash function (MD5) to hash passwords. MD5 is fast and not designed for password storage; it is susceptible to brute-force and rainbow-table attacks.

## How to reproduce (vulnerable)
1. Run the vulnerable script:
```bash
python 02-cryptographic-failures/vulnerable.py


