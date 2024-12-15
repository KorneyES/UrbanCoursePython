import sqlite3

# Создайте файл базы данных not_telegram.db и подключитесь к ней, используя встроенную библиотеку sqlite3.
conn = sqlite3.connect('not_telegram.db')

# Создайте объект курсора и выполните следующие действия при помощи SQL запросов:
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')

# Создайте таблицу Users, если она ещё не создана. В этой таблице должны присутствовать следующие поля:
# id - целое число, первичный ключ
# username - текст (не пустой)
# email - текст (не пустой)
# age - целое число
# balance - целое число (не пустой)
# Заполните её 10 записями:
users_data = [
    ('User 1', 'example1@gmail.com', 10, 1000),
    ('User 2', 'example2@gmail.com', 20, 1000),
    ('User 3', 'example3@gmail.com', 30, 1000),
    ('User 4', 'example4@gmail.com', 40, 1000),
    ('User 5', 'example5@gmail.com', 50, 1000),
    ('User 6', 'example6@gmail.com', 60, 1000),
    ('User 7', 'example7@gmail.com', 70, 1000),
    ('User 8', 'example8@gmail.com', 80, 1000),
    ('User 9', 'example9@gmail.com', 90, 1000),
    ('User 10', 'example10@gmail.com', 100, 1000),
]

cursor.executemany('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', users_data)

# Обновите balance у каждой 2ой записи начиная с 1ой на 500:
cursor.execute('UPDATE Users SET balance = balance - 500 WHERE id % 2 = 1')

# Удалите каждую 3ую запись в таблице начиная с 1ой:
cursor.execute('DELETE FROM Users WHERE id % 3 = 1')

cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != 60')
results = cursor.fetchall()

# Сделайте выборку всех записей при помощи fetchall(), где возраст не равен 60 и выведите их в консоль в следующем формате (без id):
# Имя: <username> | Почта: <email> | Возраст: <age> | Баланс: <balance>
for username, email, age, balance in results:
    print(f'Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}')

conn.commit()
conn.close()

