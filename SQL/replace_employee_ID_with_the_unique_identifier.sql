--id is the primary key (column with unique values) for this table.
--Each row of this table contains the id and the name of an employee in a company.
--(id, unique_id) is the primary key (combination of columns with unique values) for this table.
--Each row of this table contains the id and the corresponding unique id of an employee in the company.
--Write a solution to show the unique ID of each user, If a user does not have a unique ID replace just show null.
--Write your MySQL query statement below
SELECT unique_id , name
FROM Employees AS t1
LEFT JOIN EmployeeUNI AS t2 
ON t1.id = t2.id
