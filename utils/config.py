import os

# Diretório base do projeto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Caminho para o arquivo de credenciais criptografadas
CREDENTIALS_FILE = os.path.join(BASE_DIR, 'credentials/credentials.bin')
KEY_FILE = os.path.join(BASE_DIR, 'credentials/chave.key')

# URL de login
LOGIN_URL = "https://app.firstdecision.com.br/pmdecision/Login?ReturnURL=https://app.firstdecision.com.br:443/pmdecision/"