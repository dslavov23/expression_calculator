import sqlite3
from datetime import datetime


def setup_database():
    conn = sqlite3.connect("calculator.db")
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS calculations (
        id INTEGER PRIMARY KEY,
        operation CHAR(1),
        operand1 REAL,
        operand2 REAL,
        result REAL,
        timestamp TEXT
    )
    """)
    conn.commit()
    return conn


def store_calculation(conn, operation, operand1, operand2, result):
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO calculations (operation, operand1, operand2, result, timestamp)
    VALUES (?, ?, ?, ?, ?)
    """, (operation, operand1, operand2, result, datetime.now()))
    conn.commit()
