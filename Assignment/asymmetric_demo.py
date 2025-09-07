# asymmetric_demo.py
import base64
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

def b64(x: bytes) -> str:
    return base64.b64encode(x).decode()

def main():
    # 1) Plaintext
    message = "Short RSA message demo".encode("utf-8")

    # 2) Generate RSA key pair (educational)
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    # 3) Public key PEM (for evidence)
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ).decode()

    # 4) Encrypt with public key
    ciphertext = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # 5) Decrypt with private key
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # 6) Show all evidence your prof wants
    print("=== ASYMMETRIC (RSA-OAEP) DEMO ===")
    print("Public Key (PEM):\n", public_pem)
    print("Ciphertext (base64):", b64(ciphertext))
    print("Plain Input:", message.decode("utf-8"))
    print("Decrypted Output:", plaintext.decode("utf-8"))

if __name__ == "__main__":
    main()
