# ============================================================
# M11 Lesson 1 – Welcome to SQLite using Python
# ============================================================
# SQLite is a lightweight, serverless database built into Python.
# The 'sqlite3' module lets you create and manage databases
# directly from your Python code — no installation needed.
# ============================================================

import sqlite3


# ----------------------------
# Activity 1: Connect and Create a Database
# ----------------------------
# Goal: Learn how to create a SQLite database and establish a connection.
# Summary: Students will use sqlite3.connect() to create a new database
#          file and understand the role of Connection and Cursor objects.

# Task:
connection = sqlite3.connect("school.db")   # Creates school.db file
cursor = connection.cursor()                 # Cursor to execute SQL commands
print("Database connected successfully!")
connection.close()


# ----------------------------
# Activity 2: Create Your First Table
# ----------------------------
# Goal: Use CREATE TABLE to define a table structure inside the database.
# Summary: Students will write a CREATE TABLE statement using Python
#          and verify the table was created without errors.

# Task:
connection = sqlite3.connect("school.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id      INTEGER PRIMARY KEY,
        name    TEXT,
        age     INTEGER,
        grade   TEXT
    )
""")

connection.commit()
print("Table 'students' created successfully!")
connection.close()


# ----------------------------
# Activity 3: Insert Data and Fetch Records
# ----------------------------
# Goal: Insert rows into the table and retrieve them using SELECT.
# Summary: Students will use INSERT INTO to add records and fetchall()
#          to read and print all rows from the students table.

# Task:
connection = sqlite3.connect("school.db")
cursor = connection.cursor()

cursor.execute("INSERT INTO students (name, age, grade) VALUES ('Alice', 14, 'A')")
cursor.execute("INSERT INTO students (name, age, grade) VALUES ('Bob', 15, 'B')")
cursor.execute("INSERT INTO students (name, age, grade) VALUES ('Charlie', 14, 'A')")
connection.commit()

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)

connection.close()
