from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

# AES key (must be 16, 24, or 32 bytes)
KEY = b'ThisIsASecretKey'

def encrypt_data(data):
    cipher = AES.new(KEY, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(data.encode('utf-8'))

    encrypted = base64.b64encode(nonce + tag + ciphertext).decode('utf-8')
    return encrypted


def decrypt_data(encrypted_data):
    decoded = base64.b64decode(encrypted_data)

    nonce = decoded[:16]
    tag = decoded[16:32]
    ciphertext = decoded[32:]

    cipher = AES.new(KEY, AES.MODE_EAX, nonce=nonce)
    decrypted = cipher.decrypt_and_verify(ciphertext, tag)

    return decrypted.decode('utf-8')
