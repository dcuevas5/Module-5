# symmetric_demo.py
import base64
from os import urandom
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def b64(x: bytes) -> str:
    return base64.b64encode(x).decode()

def main():
    # 1) Plaintext
    message = "Hello, this is a short secret message!".encode("utf-8")

    # 2) Generate key + nonce
    key = AESGCM.generate_key(bit_length=256)  # 32 bytes
    nonce = urandom(12)                        # 96-bit nonce (GCM)

    # 3) Encrypt
    aesgcm = AESGCM(key)
    ciphertext = aesgcm.encrypt(nonce, message, None)  # AAD=None

    # 4) Decrypt (using same values)
    plaintext = aesgcm.decrypt(nonce, ciphertext, None)

    # 5) Show all evidence your prof wants
    print("=== SYMMETRIC (AES-GCM) DEMO ===")
    print("Key (base64):", b64(key))
    print("Nonce (base64):", b64(nonce))
    print("Ciphertext+Tag (base64):", b64(ciphertext))
    print("Plain Input:", message.decode("utf-8"))
    print("Decrypted Output:", plaintext.decode("utf-8"))

if __name__ == "__main__":
    main()
