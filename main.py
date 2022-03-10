import sqlite3


def task_first(my_word):
    for char in my_word:
        print(char * (ord(char.lower()) - 96))


def task_second(sql_str):
    connection = sqlite3.connect('spatial_db.db')
    cursor = connection.cursor()
    cursor.execute(sql_str)

    order_total = cursor.fetchall()
    print(order_total)


task_first('Foundry Spatial')
task_second('SELECT customer, sum(ordervalue) FROM orders GROUP BY customer;')