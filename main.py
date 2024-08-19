import os
from selenium import webdriver

from utils.config import CREDENTIALS_FILE
from utils.crypto import encrypt_credentials, decrypt_credentials
from automation.login import perform_login
from automation.navigation import navigate_to_lancamento_horas, get_last_activity_day
from automation.ponto import generate_workdays_to_launch, launch_activities


def main():
    """Ponto de entrada da aplicação."""

    # Verificar se as credenciais já estão armazenadas
    if os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, 'rb') as f:
            encrypted_credentials = f.read()
        username, password = decrypt_credentials(encrypted_credentials)
    else:
        # Solicitar as credenciais ao usuário
        username = input("Usuário: ")
        password = input("Senha: ")

        # Criptografar e armazenar as credenciais
        encrypted_credentials = encrypt_credentials(username, password)
        with open(CREDENTIALS_FILE, 'wb') as f:
            f.write(encrypted_credentials)

    # Iniciar o navegador
    driver = webdriver.Chrome()  # Ou outro navegador de sua preferência

    # Realizar o login
    if perform_login(driver, username, password):
        # Login bem-sucedido, navegue para a página de lançamento de horas
        navigate_to_lancamento_horas(driver)
        last_day = get_last_activity_day(driver)
        # Gerar os dias úteis a serem lançados
        workdays_to_launch = generate_workdays_to_launch(last_day)

        if not workdays_to_launch:
            print("Não há dias úteis a serem lançados. Encerrando o programa.")
            driver.quit()  # Fechar o navegador
            return  # Encerrar a execução do script

        launch_activities(driver, workdays_to_launch)
    else:
        # Login falhou, lide com o erro
        print("Erro no login do PMDecision. Encerrando o programa.")

    # Fechar o navegador
    driver.quit()


if __name__ == "__main__":
    main()
