from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


from utils.config import LOGIN_URL


def perform_login(driver, username, password):
    """Realiza o login no portal."""
    driver.get(LOGIN_URL)

    # Localizar e preencher os campos de usuário e senha (adaptado)
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "Login"))  # ID do campo de login
    )
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "Senha"))  # ID do campo de senha
    )

    username_field.send_keys(username)
    password_field.send_keys(password)

    # Clicar no botão de login (adaptado)
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[type='submit']"))  # Seletor CSS do botão
    )
    login_button.click()

    # Verificar se o login foi bem-sucedido
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "identificador"))
        )
        print("Login realizado com sucesso!")
        return True

    except TimeoutException:
        print("Erro: Login falhou. Verifique suas credenciais.")
        return False

    except TimeoutException:
        print("Erro: Timeout ao tentar encontrar os elementos na página de login.")
        return False
    except NoSuchElementException:
        print("Erro: Elementos da página de login não encontrados. Verifique os seletores.")
        return False
    except Exception as e:
        print(f"Ocorreu um erro inesperado durante o login: {e}")
        return False
