# 07 â€” Server-Side Request Forgery (SSRF)

## Vulnerability
Fetching arbitrary URLs from user input allows attackers to reach internal resources.

## Fix applied
- Enforce allowlists, block private IP ranges, validate/normalize URLs.

## References
- OWASP SSRF guidance.
