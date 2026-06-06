-- M10 Lesson 5 – Capstone Project – 1
-- Short Description: Build a complete database schema for a simple School Management System.

-- Activity 1
-- Goal: Create all required tables for School Management
-- Summary: Design tables - Students, Teachers, Classes, Enrollments
CREATE TABLE Teachers (
    teacher_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    subject VARCHAR(50),
    hire_date DATE
);

CREATE TABLE Classes (
    class_id INT PRIMARY KEY,
    class_name VARCHAR(50),
    teacher_id INT,
    FOREIGN KEY (teacher_id) REFERENCES Teachers(teacher_id)
);

-- Activity 2
-- Goal: Insert sample data into the tables
-- Summary: Populate the database with initial records
INSERT INTO Teachers (teacher_id, name, subject, hire_date) VALUES 
(1, 'Mr. Sharma', 'Mathematics', '2022-01-15'),
(2, 'Mrs. Gupta', 'Science', '2021-08-20');

INSERT INTO Students (id, name, age, email) VALUES 
(101, 'Rahul Kumar', 16, 'rahul@example.com');

-- Activity 3
-- Goal: Write queries to retrieve meaningful information
-- Summary: Join tables and use aggregates
SELECT 
    s.name AS student_name,
    c.class_name,
    t.name AS teacher_name
FROM Students s
JOIN Enrollments e ON s.id = e.student_id
JOIN Classes c ON e.class_id = c.class_id
JOIN Teachers t ON c.teacher_id = t.teacher_id;