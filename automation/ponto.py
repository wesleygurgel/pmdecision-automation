from datetime import date, timedelta
import calendar
import holidays

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from utils.time import generate_work_hours


def generate_workdays_to_launch(last_activity_day):
    """Gera uma lista de dias úteis a serem lançados, desde o dia seguinte à última atividade
    ou desde o primeiro dia útil do mês (se last_activity_day for None) até o dia atual."""

    today = date.today()

    if last_activity_day is None:
        # Nenhuma atividade lançada, começar do primeiro dia útil do mês
        first_day_of_month = today.replace(day=1)
        while first_day_of_month.weekday() > calendar.FRIDAY or first_day_of_month.weekday() == calendar.SUNDAY:
            first_day_of_month += timedelta(days=1)
        next_day = first_day_of_month
    else:
        # Começar do dia seguinte à última atividade lançada
        last_activity_date = today.replace(day=int(last_activity_day))
        next_day = last_activity_date + timedelta(days=1)

    workdays_to_launch = []

    # Iterar pelos dias e adicionar os dias úteis à lista
    while next_day <= today:
        if (
            next_day.weekday() not in (calendar.SATURDAY, calendar.SUNDAY)
            and next_day not in holidays.Brazil()
        ):
            workdays_to_launch.append(next_day.strftime('%d'))

        next_day += timedelta(days=1)

    print(f"Dias úteis a serem lançados: {workdays_to_launch}")
    return workdays_to_launch


def launch_activities(driver, workdays):
    """Lança as atividades para os dias úteis especificados, dividindo em manhã e tarde."""

    detalhamento = None

    for day in workdays:
        if detalhamento is None:
            # Solicitar o detalhamento da atividade ao usuário na primeira iteração
            detalhamento = input("Digite o detalhamento da atividade: ")

        else:
            # Perguntar se deseja repetir o detalhamento para os demais dias
            repetir = input(
                f"Repetir o detalhamento '{detalhamento}' para o dia {day}? (Pressione Enter para repetir, ou digite um novo detalhamento): ")
            if repetir:
                detalhamento = repetir

        # Gerar horários para o dia
        entry_time, lunch_start, lunch_end, exit_time = generate_work_hours()

        # Lançamento da manhã
        launch_activity_period(driver, day, entry_time,
                               lunch_start, detalhamento)

        # Lançamento da tarde
        launch_activity_period(driver, day, lunch_end, exit_time, detalhamento)


def launch_activity_period(driver, day, start_time, end_time, detalhamento):
    """Lança uma atividade para um período específico."""

    # Preencher o campo de data
    data_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "Dia"))
    )
    data_field.clear()  # Limpar o campo antes de preencher
    data_field.send_keys(day)

    # Preencher os campos de hora de início e término
    hora_inicio_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "HoraInicio"))
    )
    hora_termino_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "HoraTermino"))
    )

    hora_inicio_field.clear()
    hora_inicio_field.send_keys(start_time)
    hora_termino_field.clear()
    hora_termino_field.send_keys(end_time)

    # Selecionar o tipo de atividade "Desenvolvimento"
    tipo_atividade_select = Select(WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "TipoAtividadeId"))
    ))
    tipo_atividade_select.select_by_value("2117")

    # Preencher o campo de detalhamento
    detalhamento_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "Detalhamento"))
    )
    detalhamento_field.clear()
    detalhamento_field.send_keys(detalhamento)

    # Clicar no botão de salvar
    salvar_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[type='submit'].fd-btn-form"))
    )

    # Role a página até o botão antes de clicar
    actions = ActionChains(driver)
    actions.move_to_element(salvar_button).perform()

    salvar_button.click()
