from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from datetime import date, timedelta
import calendar


def navigate_to_lancamento_horas(driver):
    """Navega para a página de lançamento de horas."""

    try:
        # Localizar o botão "Timesheet" e clicar para abrir o dropdown
        timesheet_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@data-toggle='dropdown' and contains(text(), 'Timesheet')]"))
        )
        timesheet_button.click()

        # Localizar o link "Lançamento de Horas" dentro do dropdown e clicar (XPath mais específico)
        lancamento_horas_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[@href='/pmdecision/Lancamento/Create']"))
        )
        lancamento_horas_link.click()

        print("Navegou para a página de Lançamento de Horas.")

    except TimeoutException:
        print("Erro: Elementos para navegação não encontrados.")


def get_last_activity_day(driver):
    """Extrai o dia da última atividade lançada no mês."""

    try:
        # Localizar a tabela de lançamentos
        lancamentos_table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#divLancamentoNoMes table"))
        )

        # Verificar se a tabela possui linhas (está vazia ou não)
        rows = lancamentos_table.find_elements(By.XPATH, ".//tbody/tr")
        if not rows:
            return None

        # Localizar a primeira linha da tabela
        first_row = lancamentos_table.find_element(By.XPATH, ".//tbody/tr[1]")

        # Localizar a primeira coluna (dia) da primeira linha
        first_column = first_row.find_element(By.XPATH, ".//td[1]")

        # Extrair o dia da data
        data_str = first_column.text
        dia = data_str.split("/")[0]

        print(f"Dia da última atividade lançada: {dia}")
        return dia

    except NoSuchElementException:
        print("Erro: Elementos da tabela de lançamentos não encontrados.")
        return None
