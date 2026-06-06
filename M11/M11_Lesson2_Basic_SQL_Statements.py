# ============================================================
# M11 Lesson 2 – Basic SQL Statements
# ============================================================
# Core SQL statements include SELECT, INSERT, UPDATE, and DELETE.
# These are used to read, add, modify, and remove data in a table.
# ============================================================

import sqlite3

# Setup: Create and connect to database
connection = sqlite3.connect("library.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id      INTEGER PRIMARY KEY AUTOINCREMENT,
        title   TEXT,
        author  TEXT,
        year    INTEGER,
        genre   TEXT
    )
""")
connection.commit()


# ----------------------------
# Activity 1: INSERT and SELECT
# ----------------------------
# Goal: Add multiple records and retrieve them using SELECT queries.
# Summary: Students will insert at least 5 book records and use
#          SELECT with and without conditions to view the data.

# Task:
cursor.executemany("INSERT INTO books (title, author, year, genre) VALUES (?, ?, ?, ?)", [
    ("The Alchemist",      "Paulo Coelho",   1988, "Fiction"),
    ("Harry Potter",       "J.K. Rowling",   1997, "Fantasy"),
    ("Clean Code",         "Robert Martin",  2008, "Technology"),
    ("Atomic Habits",      "James Clear",    2018, "Self-Help"),
    ("The Great Gatsby",   "F. Scott",       1925, "Classic"),
])
connection.commit()

cursor.execute("SELECT * FROM books")
print("All Books:", cursor.fetchall())

cursor.execute("SELECT title, author FROM books WHERE genre = 'Fiction'")
print("Fiction Books:", cursor.fetchall())


# ----------------------------
# Activity 2: UPDATE Records
# ----------------------------
# Goal: Modify existing records in the table using the UPDATE statement.
# Summary: Students will update specific fields of a record using
#          WHERE clause to target the correct row.

# Task:
cursor.execute("UPDATE books SET year = 1997 WHERE title = 'Harry Potter'")
cursor.execute("UPDATE books SET genre = 'Classic Fiction' WHERE author = 'F. Scott'")
connection.commit()

cursor.execute("SELECT * FROM books WHERE title = 'Harry Potter'")
print("Updated Harry Potter:", cursor.fetchone())


# ----------------------------
# Activity 3: DELETE Records and Use ORDER BY
# ----------------------------
# Goal: Remove records from the table and sort query results.
# Summary: Students will delete a specific book using DELETE and
#          practice ordering results with ORDER BY ASC and DESC.

# Task:
cursor.execute("DELETE FROM books WHERE title = 'The Great Gatsby'")
connection.commit()

cursor.execute("SELECT * FROM books ORDER BY year ASC")
print("Books by Year (ASC):", cursor.fetchall())

cursor.execute("SELECT * FROM books ORDER BY title DESC")
print("Books by Title (DESC):", cursor.fetchall())

connection.close()
