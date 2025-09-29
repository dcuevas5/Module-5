# 04 â€” NoSQL Injection

## Vulnerability
Trusting user-supplied query objects directly can allow NoSQL operators or crafted payloads to change query semantics.

## Fix applied
- Validate and sanitize inputs; use allowlists for fields and types.

## References
- OWASP: NoSQL Injection guidance.
