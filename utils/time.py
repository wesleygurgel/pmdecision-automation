import random
from datetime import datetime, timedelta

def generate_time(start, end):
    """Gera um horário aleatório dentro do intervalo especificado."""
    start_time = datetime.strptime(start, "%H:%M")
    end_time = datetime.strptime(end, "%H:%M")
    random_time = start_time + timedelta(minutes=random.randint(0, int((end_time - start_time).seconds / 60)))
    return random_time.strftime("%H:%M")

def generate_work_hours():
    """Gera os horários de entrada, almoço e saída para um dia de trabalho."""

    entry_time = generate_time("08:45", "09:15")
    lunch_start = generate_time("11:30", "14:00")
    lunch_end = (datetime.strptime(lunch_start, "%H:%M") + timedelta(hours=1)).strftime("%H:%M")

    # Correção no cálculo do exit_time
    entry_datetime = datetime.strptime(entry_time, "%H:%M")
    lunch_start_datetime = datetime.strptime(lunch_start, "%H:%M")
    lunch_end_datetime = datetime.strptime(lunch_end, "%H:%M")
    work_duration = timedelta(hours=8)
    lunch_duration = lunch_end_datetime - lunch_start_datetime
    exit_time = (entry_datetime + work_duration + lunch_duration).strftime("%H:%M")

    print(f"Horários gerados: Entrada: {entry_time}, Almoço: {lunch_start} - {lunch_end}, Saída: {exit_time}")

    return entry_time, lunch_start, lunch_end, exit_time