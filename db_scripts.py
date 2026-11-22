import sqlite3

from settings import *

conn = None
cursor = None


def open_db():
    global conn, cursor
    conn = sqlite3.connect(PATH_DB)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('PRAGMA foreign_keys = ON')


def close_db():
    if cursor:
        cursor.close()
    if conn:
        conn.close()


def execute(query, params=None):
    if params is None:
        cursor.execute(query)
    else:
        cursor.execute(query, params)
    conn.commit()


def create_table():
    open_db()

    execute('''
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name STRING,
            age INTEGER,
            major STRING
        )
    ''')

    execute('''
        CREATE TABLE IF NOT EXISTS courses(
            course_id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_name STRING,
            instructor STRING
        )
    ''')

    execute('''
        CREATE TABLE IF NOT EXISTS student_courses(
            student_id INTEGER,
            course_id INTEGER,
            FOREIGN KEY (student_id) REFERENCES student(id),
            FOREIGN KEY (course_id) REFERENCES course(course_id)
        )
    ''')

    close_db()
