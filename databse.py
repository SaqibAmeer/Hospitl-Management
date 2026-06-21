import sqlite3


def connect():
    return sqlite3.connect("hospital.db")


def create_tables():
    db = connect()
    cursor = db.cursor()
    cursor.execute("""
  CREATE TABLE IF NOT EXISTS patients(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        disease TEXT

    )
    """)



    cursor.execute("""
    CREATE TABLE IF NOT EXISTS doctors(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        speciality TEXT

    )
    """)



    cursor.execute("""
    CREATE TABLE IF NOT EXISTS appointments(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER,
        doctor_id INTEGER,
        date TEXT

    )
    """)



    cursor.execute("""
    CREATE TABLE IF NOT EXISTS records(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER,
        diagnosis TEXT,
        medicine TEXT

    )
    """)



    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bills(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER,
        amount REAL

    )
    """)



    db.commit()
    db.close()