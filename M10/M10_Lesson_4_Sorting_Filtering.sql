-- M10 Lesson 4 – SQL- SORTING & FILTERING
-- Short Description: Learn how to filter data using WHERE clause and sort using ORDER BY.

-- Activity 1
-- Goal: Apply different WHERE conditions for filtering
-- Summary: Filter records based on multiple criteria
SELECT * FROM Students 
WHERE age BETWEEN 15 AND 25 
AND city = 'Mumbai' 
AND grade IN ('A', 'B');

-- Activity 2
-- Goal: Sort data in ascending and descending order
-- Summary: Sort employees by salary and name
SELECT * FROM Employees 
ORDER BY salary DESC, first_name ASC;

-- Activity 3
-- Goal: Combine filtering and sorting with LIMIT
-- Summary: Get top 5 highest paid employees in a department
SELECT * FROM Employees 
WHERE department = 'IT'
ORDER BY salary DESC
LIMIT 5;