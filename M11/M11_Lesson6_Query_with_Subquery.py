# ============================================================
# M11 Lesson 6 – Query with Subquery
# ============================================================
# A Subquery is a query nested inside another query.
# It can be used in SELECT, WHERE, FROM, and HAVING clauses
# to perform multi-step data retrieval in a single statement.
# ============================================================

import sqlite3

# Setup
connection = sqlite3.connect("subquery_demo.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id         INTEGER PRIMARY KEY,
        name       TEXT,
        department TEXT,
        salary     REAL
    )
""")

cursor.executemany("INSERT OR IGNORE INTO employees VALUES (?, ?, ?, ?)", [
    (1,  "Alice",   "Engineering", 80000),
    (2,  "Bob",     "Engineering", 95000),
    (3,  "Charlie", "Marketing",   60000),
    (4,  "Diana",   "Marketing",   72000),
    (5,  "Eve",     "HR",          55000),
    (6,  "Frank",   "HR",          62000),
    (7,  "Grace",   "Engineering", 90000),
    (8,  "Hank",    "Marketing",   68000),
])
connection.commit()


# ----------------------------
# Activity 1: Subquery in WHERE Clause
# ----------------------------
# Goal: Use a subquery inside WHERE to filter based on computed values.
# Summary: Students will write subqueries to find employees whose
#          salary is above the company average or department average.

# Task:
cursor.execute("""
    SELECT name, salary
    FROM employees
    WHERE salary > (SELECT AVG(salary) FROM employees)
""")
print("Employees above company average salary:")
for row in cursor.fetchall():
    print(" ", row)

cursor.execute("""
    SELECT name, department, salary
    FROM employees
    WHERE salary = (SELECT MAX(salary) FROM employees)
""")
print("\nHighest paid employee:", cursor.fetchall())


# ----------------------------
# Activity 2: Subquery in FROM Clause
# ----------------------------
# Goal: Use a subquery as a temporary table inside the FROM clause.
# Summary: Students will create a derived table using a subquery and
#          query it just like a regular table.

# Task:
cursor.execute("""
    SELECT department, avg_sal
    FROM (
        SELECT department, AVG(salary) as avg_sal
        FROM employees
        GROUP BY department
    ) AS dept_averages
    WHERE avg_sal > 65000
""")
print("\nDepartments with avg salary > 65000:")
for row in cursor.fetchall():
    print(" ", row)


# ----------------------------
# Activity 3: Subquery with IN and EXISTS
# ----------------------------
# Goal: Use IN and EXISTS with subqueries for advanced filtering.
# Summary: Students will use IN to match against a list from a subquery
#          and EXISTS to check for related records in another table.

# Task:

# Find top-2 salary earners using subquery with IN:
cursor.execute("""
    SELECT name, salary
    FROM employees
    WHERE salary IN (
        SELECT salary FROM employees ORDER BY salary DESC LIMIT 2
    )
""")
print("\nTop 2 salary earners:")
for row in cursor.fetchall():
    print(" ", row)

# Find departments where at least one employee earns > 85000:
cursor.execute("""
    SELECT DISTINCT department
    FROM employees e1
    WHERE EXISTS (
        SELECT 1 FROM employees e2
        WHERE e2.department = e1.department AND e2.salary > 85000
    )
""")
print("\nDepartments with at least one employee earning > 85000:")
for row in cursor.fetchall():
    print(" ", row)

connection.close()
