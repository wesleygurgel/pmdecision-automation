from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

import base64
import os
from utils.config import KEY_FILE


def generate_key():
    """Gera ou carrega a chave de criptografia."""

    if os.path.exists(KEY_FILE):
        # A chave já existe, então carregue-a do arquivo
        with open(KEY_FILE, "rb") as key_file:
            key = key_file.read()
    else:
        # A chave não existe, então gere uma nova e salve-a no arquivo
        password = b"sua_senha_forte_aqui"  # Substitua por uma senha forte
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=390000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))

        with open(KEY_FILE,
                  "wb") as key_file:
            key_file.write(key)

        print(
            f"Chave de criptografia gerada e salva em {KEY_FILE}. Guarde-a em um local seguro!")

    return key


def load_key():
    """Carrega a chave de criptografia de um local seguro."""
    with open("credentials/chave.key", "rb") as key_file:
        key = key_file.read()
    return key


def encrypt_credentials(username, password):
    """Criptografa as credenciais."""
    key = generate_key()
    f = Fernet(key)
    token = f.encrypt(f"{username}:{password}".encode())
    return token


def decrypt_credentials(token):
    """Descriptografa as credenciais."""
    key = load_key()
    f = Fernet(key)
    decrypted_data = f.decrypt(token).decode()
    username, password = decrypted_data.split(":")
    return username, password
