import sqlite3

conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()

# Удалите из базы данных not_telegram.db запись с id = 6.
cursor.execute('DELETE FROM Users WHERE id = 6')

# Подсчитать общее количество записей.
cursor.execute('SELECT COUNT(*) FROM Users')
total_records = cursor.fetchone()[0]
print(f'Общее количество записей: {total_records}')

# Посчитать сумму всех балансов.
cursor.execute('SELECT SUM(balance) FROM Users')
total_balance = cursor.fetchone()[0]

# Вывести в консоль средний баланс всех пользователей.
if total_records > 0:
    average_balance = total_balance / total_records
    print(f'Средний баланс всех пользователей: {average_balance:.2f}')
else:
    print('Нет пользователей в базе данных.')

conn.commit()
conn.close()
