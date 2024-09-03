team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 18015.2
team2_time = 17000.0
tasks_total = 82
time_avg = 350.4


# 1. Количество участников первой команды
result1 = "В команде Мастера кода участников: %d !" % team1_num                                                         # Использование %
print(result1)

# 2. Количество участников в обеих командах
result2 = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)
print(result2)

# 3. Количество задач решённых командой 2
result3 = "Команда Волшебники данных решила задач: {} !".format(score_2)                                                # Использование format()
print(result3)

# 4. Время за которое команда 2 решила задачи
result4 = "Волшебники данных решили задачи за {} с !".format(team1_time)
print(result4)

# 5. Количество решённых задач по командам
result5 = f"Команды решили {score_1} и {score_2} задач."                                                                # Использование f-строк
print(result5)

# 6. Исход соревнования
if score_1 > score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'

result6 = f"Результат битвы: {challenge_result}"
print(result6)

# 7. Количество задач и среднее время решения
result7 = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!."
print(result7)

import os
import time

# Укажите директорию, которую хотите обойти
directory = "."

# Обход каталога с использованием os.walk
for root, dirs, files in os.walk(directory):
    for file in files:
        # Формирование полного пути к файлу
        filepath = os.path.join(root, file)

        # Получение времени последнего изменения файла
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

        # Получение размера файла
        filesize = os.path.getsize(filepath)

        # Получение родительской директории
        parent_dir = os.path.dirname(filepath)

        # Вывод информации о файле
        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')


