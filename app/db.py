import sqlite3

conn = sqlite3.connect("saved.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chat_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        num_phone TEXT NOT NULL
)
''')
conn.commit()
conn.close()


def saved_db(student_data):
    conn = sqlite3.connect("saved.db")
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO students (chat_id, name, age, num_phone)
    VALUES(?, ?, ?, ?)
'''(
    student_data['chat_id'],
    student_data['name'],
    student_data['age'],
    student_data['num_phone'],
))
    conn.commit()
    conn.close()
