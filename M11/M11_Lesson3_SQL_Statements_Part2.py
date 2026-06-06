# ============================================================
# M11 Lesson 3 – SQL Statements – Part 2
# ============================================================
# This lesson covers filtering with WHERE, LIKE, BETWEEN,
# aggregate functions (COUNT, SUM, AVG), and GROUP BY clause.
# ============================================================

import sqlite3

# Setup
connection = sqlite3.connect("products.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id       INTEGER PRIMARY KEY AUTOINCREMENT,
        name     TEXT,
        category TEXT,
        price    REAL,
        stock    INTEGER
    )
""")

cursor.executemany("INSERT INTO products (name, category, price, stock) VALUES (?, ?, ?, ?)", [
    ("Laptop",      "Electronics", 75000, 10),
    ("Phone",       "Electronics", 30000, 25),
    ("Headphones",  "Electronics", 3000,  50),
    ("T-Shirt",     "Clothing",    500,   100),
    ("Jeans",       "Clothing",    1500,  60),
    ("Rice 5kg",    "Food",        300,   200),
    ("Olive Oil",   "Food",        800,   80),
])
connection.commit()


# ----------------------------
# Activity 1: WHERE, LIKE, and BETWEEN
# ----------------------------
# Goal: Filter records using WHERE conditions, LIKE patterns, and BETWEEN range.
# Summary: Students will write queries to search for records matching
#          specific conditions using different filtering techniques.

# Task:
cursor.execute("SELECT * FROM products WHERE price > 1000")
print("Price > 1000:", cursor.fetchall())

cursor.execute("SELECT * FROM products WHERE name LIKE '%a%'")
print("Name contains 'a':", cursor.fetchall())

cursor.execute("SELECT * FROM products WHERE price BETWEEN 500 AND 5000")
print("Price between 500-5000:", cursor.fetchall())

cursor.execute("SELECT * FROM products WHERE category = 'Electronics' AND price < 50000")
print("Electronics under 50k:", cursor.fetchall())


# ----------------------------
# Activity 2: Aggregate Functions
# ----------------------------
# Goal: Use COUNT, SUM, AVG, MAX, and MIN to summarize table data.
# Summary: Students will apply aggregate functions to get useful
#          statistics about the products in the table.

# Task:
cursor.execute("SELECT COUNT(*) FROM products")
print("Total Products:", cursor.fetchone()[0])

cursor.execute("SELECT SUM(price) FROM products WHERE category = 'Electronics'")
print("Total Electronics Cost:", cursor.fetchone()[0])

cursor.execute("SELECT AVG(price) FROM products")
print("Average Price:", cursor.fetchone()[0])

cursor.execute("SELECT MAX(price), MIN(price) FROM products")
print("Max & Min Price:", cursor.fetchone())


# ----------------------------
# Activity 3: GROUP BY and HAVING
# ----------------------------
# Goal: Group records by category and filter groups using HAVING.
# Summary: Students will use GROUP BY to summarize data per category
#          and HAVING to filter grouped results by a condition.

# Task:
cursor.execute("SELECT category, COUNT(*) as total FROM products GROUP BY category")
print("Products per Category:", cursor.fetchall())

cursor.execute("SELECT category, AVG(price) as avg_price FROM products GROUP BY category")
print("Avg Price per Category:", cursor.fetchall())

cursor.execute("""
    SELECT category, SUM(stock) as total_stock
    FROM products
    GROUP BY category
    HAVING total_stock > 100
""")
print("Categories with stock > 100:", cursor.fetchall())

connection.close()
