# ============================================================
# M11 Lesson 5 – Joins in SQL
# ============================================================
# JOINs combine rows from two or more tables based on a related
# column. Types: INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL JOIN.
# ============================================================

import sqlite3

# Setup: Create two related tables
connection = sqlite3.connect("joins_demo.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        customer_id   INTEGER PRIMARY KEY,
        customer_name TEXT,
        city          TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        order_id    INTEGER PRIMARY KEY,
        customer_id INTEGER,
        product     TEXT,
        amount      REAL
    )
""")

cursor.executemany("INSERT OR IGNORE INTO customers VALUES (?, ?, ?)", [
    (1, "Alice",   "Delhi"),
    (2, "Bob",     "Mumbai"),
    (3, "Charlie", "Pune"),
    (4, "Diana",   "Chennai"),   # No orders
])

cursor.executemany("INSERT OR IGNORE INTO orders VALUES (?, ?, ?, ?)", [
    (101, 1, "Laptop",     75000),
    (102, 1, "Mouse",      500),
    (103, 2, "Phone",      30000),
    (104, 3, "Headphones", 3000),
    (105, 5, "Keyboard",   1500),  # Customer 5 doesn't exist
])
connection.commit()


# ----------------------------
# Activity 1: INNER JOIN
# ----------------------------
# Goal: Retrieve only the matching rows from both tables using INNER JOIN.
# Summary: Students will use INNER JOIN to get records where there is
#          a match in both the customers and orders tables.

# Task:
cursor.execute("""
    SELECT customers.customer_name, orders.product, orders.amount
    FROM customers
    INNER JOIN orders ON customers.customer_id = orders.customer_id
""")
print("INNER JOIN Result:")
for row in cursor.fetchall():
    print(" ", row)


# ----------------------------
# Activity 2: LEFT JOIN
# ----------------------------
# Goal: Retrieve all rows from the left table, with NULLs for no match.
# Summary: Students will use LEFT JOIN to list all customers including
#          those who haven't placed any orders yet.

# Task:
cursor.execute("""
    SELECT customers.customer_name, orders.product, orders.amount
    FROM customers
    LEFT JOIN orders ON customers.customer_id = orders.customer_id
""")
print("\nLEFT JOIN Result (all customers):")
for row in cursor.fetchall():
    print(" ", row)

# Find customers who have NOT placed any order:
cursor.execute("""
    SELECT customers.customer_name
    FROM customers
    LEFT JOIN orders ON customers.customer_id = orders.customer_id
    WHERE orders.order_id IS NULL
""")
print("\nCustomers with NO Orders:", cursor.fetchall())


# ----------------------------
# Activity 3: JOIN with Aggregation
# ----------------------------
# Goal: Combine JOIN with GROUP BY and aggregate functions.
# Summary: Students will calculate total spending per customer
#          by combining INNER JOIN with SUM and GROUP BY.

# Task:
cursor.execute("""
    SELECT customers.customer_name, COUNT(orders.order_id) as total_orders,
           SUM(orders.amount) as total_spent
    FROM customers
    INNER JOIN orders ON customers.customer_id = orders.customer_id
    GROUP BY customers.customer_name
    ORDER BY total_spent DESC
""")
print("\nTotal Spending per Customer:")
for row in cursor.fetchall():
    print(" ", row)

connection.close()
