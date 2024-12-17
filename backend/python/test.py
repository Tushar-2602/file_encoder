import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

password = "password".encode()
salt = b'\xe2\xaf\xbc:\xdd'
key1 = Fernet.generate_key()
f1 = Fernet(key1)
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=390000,
)
key = base64.urlsafe_b64encode(kdf.derive(password))
f = Fernet(key)
token = b'gAAAAABnYWJyDPKBqYddLE8kgnpFRW-BcLYTWXB8pTLO17SPJr8h2ZSyIYeGgN1Bu6xg6deWDlsVekqYTzJskJNvtnztQ0lktg=='
print(token)

# b'...'
try:
 print((f.decrypt(token)).decode())
except Exception:
 print("worng key")
# b'Secret message!'