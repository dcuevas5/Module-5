$base = (Get-Location).Path

function Write-Note($relPath, $content) {
  $full = Join-Path $base $relPath
  $dir = Split-Path $full -Parent
  if (-not (Test-Path $dir)) { New-Item -ItemType Directory -Path $dir -Force | Out-Null }
  $content | Out-File -FilePath $full -Encoding UTF8
  Write-Host "Wrote: $relPath"
}

# 03 - SQL Injection
$note03 = @'
# 03 — SQL Injection

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
'@
Write-Note "03-sql-injection/notes.md" $note03

# 04 - NoSQL Injection
$note04 = @'
# 04 — NoSQL Injection

## Vulnerability
Trusting user-supplied query objects directly can allow NoSQL operators or crafted payloads to change query semantics.

## Fix applied
- Validate and sanitize inputs; use allowlists for fields and types.

## References
- OWASP: NoSQL Injection guidance.
'@
Write-Note "04-nosql-injection/notes.md" $note04

# 05 - Insecure Design
$note05 = @'
# 05 — Insecure Design

## Vulnerability
Sensitive actions are performed without verification (e.g., resetting passwords directly).

## Fix applied
- Implement token-based verification and expiration for sensitive flows.

## References
- OWASP: Insecure Design guidance.
'@
Write-Note "05-insecure-design/notes.md" $note05

# 06 - Software and Data Integrity
$note06 = @'
# 06 — Software & Data Integrity Failures

## Vulnerability
Including third-party scripts without integrity checks risks supply-chain attacks.

## Fix applied
- Use SRI, CSP, and verify third-party signatures.

## References
- OWASP: Software Supply Chain.
'@
Write-Note "06-software-data-integrity/notes.md" $note06

# 07 - SSRF
$note07 = @'
# 07 — Server-Side Request Forgery (SSRF)

## Vulnerability
Fetching arbitrary URLs from user input allows attackers to reach internal resources.

## Fix applied
- Enforce allowlists, block private IP ranges, validate/normalize URLs.

## References
- OWASP SSRF guidance.
'@
Write-Note "07-ssrf/notes.md" $note07

# 08 - Identification & Authentication
$note08 = @'
# 08 — Identification & Authentication Failures

## Vulnerability
Plaintext password comparison and no adaptive hashing.

## Fix applied
- Use bcrypt/Argon2, secure comparison, rate limiting.

## References
- OWASP Authentication Cheat Sheet.
'@
Write-Note "08-identification-authentication/notes.md" $note08

# 09 - Configuration & Headers
$note09 = @'
# 09 — Security Misconfiguration & Security Headers

## Vulnerability
Missing security headers and insecure defaults.

## Fix applied
- Add CSP, X-Frame-Options, X-Content-Type-Options and harden server config.

## References
- OWASP Secure Headers guidance.
'@
Write-Note "09-configuration-and-headers/notes.md" $note09

# 10 - Logging & Monitoring
$note10 = @'
# 10 — Logging and Monitoring

## Vulnerability
No logging or logging secrets; no detection.

## Fix applied
- Implement proper logging, avoid secrets, set levels and alerts.

## References
- OWASP Logging and Monitoring guidance.
'@
Write-Note "10-logging-and-monitoring/notes.md" $note10

Write-Host "`nAll notes created. Review the files and commit changes."
