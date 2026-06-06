# ============================================================
# M11 Lesson 4 – SQL Constraints
# ============================================================
# Constraints enforce rules on data in a table to maintain
# accuracy and integrity. Common constraints: NOT NULL, UNIQUE,
# PRIMARY KEY, DEFAULT, CHECK, and FOREIGN KEY.
# ============================================================

import sqlite3


# ----------------------------
# Activity 1: NOT NULL, UNIQUE, and DEFAULT
# ----------------------------
# Goal: Understand and apply NOT NULL, UNIQUE, and DEFAULT constraints.
# Summary: Students will create a table with these constraints and
#          test what happens when rules are violated.

# Task:
connection = sqlite3.connect("constraints_demo.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id         INTEGER PRIMARY KEY AUTOINCREMENT,
        name       TEXT NOT NULL,
        email      TEXT UNIQUE,
        department TEXT DEFAULT 'General',
        salary     REAL NOT NULL
    )
""")

cursor.execute("INSERT INTO employees (name, email, salary) VALUES ('Alice', 'alice@co.com', 50000)")
cursor.execute("INSERT INTO employees (name, email, salary) VALUES ('Bob', 'bob@co.com', 60000)")
connection.commit()

cursor.execute("SELECT * FROM employees")
print("Employees:", cursor.fetchall())

# Uncomment to test NOT NULL violation:
# cursor.execute("INSERT INTO employees (email, salary) VALUES ('test@co.com', 40000)")

connection.close()


# ----------------------------
# Activity 2: CHECK Constraint
# ----------------------------
# Goal: Use the CHECK constraint to enforce value rules in a column.
# Summary: Students will add a CHECK constraint to ensure only valid
#          data (e.g., positive salary, valid age) is inserted.

# Task:
connection = sqlite3.connect("constraints_demo.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id    INTEGER PRIMARY KEY AUTOINCREMENT,
        name  TEXT NOT NULL,
        age   INTEGER CHECK(age >= 5 AND age <= 25),
        marks INTEGER CHECK(marks >= 0 AND marks <= 100)
    )
""")

cursor.execute("INSERT INTO students (name, age, marks) VALUES ('Charlie', 15, 88)")
cursor.execute("INSERT INTO students (name, age, marks) VALUES ('Diana', 17, 95)")
connection.commit()

cursor.execute("SELECT * FROM students")
print("Students:", cursor.fetchall())

# Uncomment to test CHECK violation:
# cursor.execute("INSERT INTO students (name, age, marks) VALUES ('Eve', 3, 110)")

connection.close()


# ----------------------------
# Activity 3: FOREIGN KEY Constraint
# ----------------------------
# Goal: Link two tables using FOREIGN KEY to maintain referential integrity.
# Summary: Students will create two related tables (departments and staff)
#          and understand how FOREIGN KEY prevents orphan records.

# Task:
connection = sqlite3.connect("constraints_demo.db")
connection.execute("PRAGMA foreign_keys = ON")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS departments (
        dept_id   INTEGER PRIMARY KEY,
        dept_name TEXT NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS staff (
        staff_id  INTEGER PRIMARY KEY AUTOINCREMENT,
        name      TEXT NOT NULL,
        dept_id   INTEGER,
        FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
    )
""")

cursor.execute("INSERT INTO departments VALUES (1, 'Engineering')")
cursor.execute("INSERT INTO departments VALUES (2, 'Marketing')")
cursor.execute("INSERT INTO staff (name, dept_id) VALUES ('Ravi', 1)")
cursor.execute("INSERT INTO staff (name, dept_id) VALUES ('Priya', 2)")
connection.commit()

cursor.execute("SELECT staff.name, departments.dept_name FROM staff JOIN departments ON staff.dept_id = departments.dept_id")
print("Staff with Departments:", cursor.fetchall())

connection.close()
