-- M10 Lesson 3 – SQL-AGRREGATE FUNCTIONS
-- Short Description: Learn aggregate functions like COUNT, SUM, AVG, MIN, MAX and GROUP BY.

-- Activity 1
-- Goal: Use basic aggregate functions on a table
-- Summary: Calculate total, average, min and max salary
SELECT 
    COUNT(*) AS total_employees,
    SUM(salary) AS total_salary,
    AVG(salary) AS avg_salary,
    MIN(salary) AS min_salary,
    MAX(salary) AS max_salary
FROM Employees;

-- Activity 2
-- Goal: Use GROUP BY with aggregate functions
-- Summary: Find department-wise statistics
SELECT 
    department,
    COUNT(*) AS emp_count,
    AVG(salary) AS avg_salary
FROM Employees
GROUP BY department;

-- Activity 3
-- Goal: Combine HAVING clause with aggregates
-- Summary: Filter groups based on aggregate conditions
SELECT 
    department,
    COUNT(*) AS emp_count,
    SUM(salary) AS total_salary
FROM Employees
GROUP BY department
HAVING COUNT(*) > 5 AND SUM(salary) > 500000;