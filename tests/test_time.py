import unittest
from utils.time import generate_time, generate_work_hours
from datetime import datetime, timedelta

class TestUtils(unittest.TestCase):

    def test_generate_time(self):
        """Testa se generate_time gera um horário dentro do intervalo esperado."""

        # Testa com alguns intervalos
        for _ in range(10):  # Repete o teste algumas vezes para verificar a aleatoriedade
            generated_time = generate_time("08:00", "10:00")
            self.assertTrue("08:00" <= generated_time <= "10:00")

            generated_time = generate_time("13:30", "14:15")
            self.assertTrue("13:30" <= generated_time <= "14:15")

    def test_generate_work_hours(self):
        """Testa se generate_work_hours gera horários válidos e com duração total de trabalho correta."""

        for _ in range(10): 
            entry_time, lunch_start, lunch_end, exit_time = generate_work_hours()

            # Verificar se os horários estão dentro dos intervalos esperados
            self.assertTrue("08:45" <= entry_time <= "09:15")
            self.assertTrue("11:30" <= lunch_start <= "14:00")
            self.assertTrue("12:30" <= lunch_end <= "15:00")  # 1 hora após lunch_start

            # Verificar a duração total do trabalho (8 horas)
            entry_datetime = datetime.strptime(entry_time, "%H:%M")
            lunch_start_datetime = datetime.strptime(lunch_start, "%H:%M")
            lunch_end_datetime = datetime.strptime(lunch_end, "%H:%M")
            exit_datetime = datetime.strptime(exit_time, "%H:%M")

            work_duration_morning = lunch_start_datetime - entry_datetime
            work_duration_afternoon = exit_datetime - lunch_end_datetime
            total_work_duration = work_duration_morning + work_duration_afternoon

            self.assertEqual(total_work_duration, timedelta(hours=8))

if __name__ == '__main__':
    unittest.main()