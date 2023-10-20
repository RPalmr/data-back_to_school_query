# pylint:disable=C0111,C0103

# import sqlite3
# conn = sqlite3.connect('data/school.sqlite')
# db = conn.cursor()


def students_from_city(db_cursor, city):
    """return a list of students from a specific city"""
    query = "SELECT * FROM students WHERE birth_city = ?"
    db_cursor.execute(query, (city,))
    return db_cursor.fetchall()

print(students_from_city(db, 'Paris'))
