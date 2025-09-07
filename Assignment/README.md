# Symmetric (AES-GCM) and Asymmetric (RSA-OAEP) Encryption — Python

This repository demonstrates basic encryption/decryption using:
- **Symmetric:** AES-GCM (confidentiality plus integrity via authentication tag)
- **Asymmetric:** RSA-OAEP with SHA-256 (modern padding; suited for short messages and key exchange)

## Requirements
- Python 3.10+ (recommended)
- `cryptography==43.0.1`

## Setup
```bash
python -m venv .venv
# Windows
.\.venv\Scripts\Activate.ps1
pip install cryptography==43.0.1
