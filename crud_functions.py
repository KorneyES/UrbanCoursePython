# Создайте файл crud_functions.py и напишите там следующие функции:

import sqlite3

def initiate_db():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

# initiate_db, которая создаёт таблицу Products, если она ещё не создана при помощи SQL запроса. Эта таблица должна содержать следующие поля:
# id - целое число, первичный ключ
# title(название продукта) - текст (не пустой)
# description(описание) - текст
# price(цена) - целое число (не пустой)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

# get_all_products, которая возвращает все записи из таблицы Products, полученные при помощи SQL запроса.
def get_all_products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Получение всех записей из таблицы Products
    cursor.execute('SELECT title, description, price FROM Products')
    products = cursor.fetchall()

    conn.close()
    return products

def populate_db():
    products = [
        ("Product1", "Описание 1", 100),
        ("Product2", "Описание 2", 200),
        ("Product3", "Описание 3", 300),
        ("Product4", "Описание 4", 400),
    ]

    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.executemany('''
        INSERT INTO Products (title, description, price) VALUES (?, ?, ?)
    ''', products)

    conn.commit()
    conn.close()

populate_db()




