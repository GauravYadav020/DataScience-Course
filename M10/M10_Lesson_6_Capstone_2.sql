-- M10 Lesson 6 – Capstone Project – 2
-- Short Description: Advanced queries and database operations for Library Management System.

-- Activity 1
-- Goal: Create Library related tables with proper relationships
-- Summary: Books, Members, Issuance tables
CREATE TABLE Books (
    book_id INT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    author VARCHAR(100),
    copies_available INT DEFAULT 1
);

CREATE TABLE Members (
    member_id INT PRIMARY KEY,
    name VARCHAR(100),
    join_date DATE
);

CREATE TABLE Issuances (
    issuance_id INT PRIMARY KEY,
    book_id INT,
    member_id INT,
    issue_date DATE,
    return_date DATE,
    FOREIGN KEY (book_id) REFERENCES Books(book_id),
    FOREIGN KEY (member_id) REFERENCES Members(member_id)
);

-- Activity 2
-- Goal: Perform complex queries using JOINs and aggregates
-- Summary: Find most issued books and overdue returns
SELECT 
    b.title,
    COUNT(i.issuance_id) AS times_issued
FROM Books b
LEFT JOIN Issuances i ON b.book_id = i.book_id
GROUP BY b.title
ORDER BY times_issued DESC;

-- Activity 3
-- Goal: Update and manage data with real-world scenarios
-- Summary: Update book copies and mark returns
UPDATE Books SET copies_available = copies_available - 1 WHERE book_id = 5;

UPDATE Issuances SET return_date = CURRENT_DATE 
WHERE issuance_id = 10 AND return_date IS NULL;