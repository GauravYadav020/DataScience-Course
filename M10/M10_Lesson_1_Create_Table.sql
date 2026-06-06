-- M10 Lesson 1 – SQL- Create Table
-- Short Description: Learn how to create tables in SQL using CREATE TABLE statement with proper data types and constraints.

-- Activity 1
-- Goal: Understand basic table creation with different data types
-- Summary: Create a simple 'Students' table with columns like id, name, age, email
CREATE TABLE Students (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    email VARCHAR(100)
);

-- Activity 2
-- Goal: Practice adding constraints like NOT NULL, UNIQUE, and DEFAULT
-- Summary: Create an 'Employees' table with various constraints
CREATE TABLE Employees (
    emp_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    salary DECIMAL(10,2) DEFAULT 0.00,
    hire_date DATE UNIQUE
);

-- Activity 3
-- Goal: Create a table with foreign key relationship
-- Summary: Create 'Orders' table that references 'Customers' table
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100)
);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);