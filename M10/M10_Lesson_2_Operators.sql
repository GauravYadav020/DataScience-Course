-- M10 Lesson 2 – SQL-OPERATORS
-- Short Description: Learn various SQL operators like Arithmetic, Comparison, Logical, and Special operators.

-- Activity 1
-- Goal: Practice Arithmetic and Comparison Operators
-- Summary: Write queries using +, -, *, /, =, >, < etc. on sample data
SELECT 
    10 + 5 AS addition,
    20 - 8 AS subtraction,
    5 * 4 AS multiplication,
    100 / 2 AS division;

SELECT * FROM Employees WHERE salary > 50000;

-- Activity 2
-- Goal: Use Logical Operators (AND, OR, NOT)
-- Summary: Filter data using multiple conditions
SELECT * FROM Students 
WHERE age >= 18 AND (email IS NOT NULL OR city = 'Delhi');

-- Activity 3
-- Goal: Explore Special Operators (LIKE, IN, BETWEEN)
-- Summary: Use pattern matching and range queries
SELECT * FROM Employees 
WHERE first_name LIKE 'A%' 
AND salary BETWEEN 30000 AND 80000 
AND department IN ('IT', 'HR');