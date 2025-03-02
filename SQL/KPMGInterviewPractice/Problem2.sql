
/*

CREATE TABLE Employees
(
employee_id	 INT,
name	VARCHAR(40),
salary	INT,
department_id INT
) ;

INSERT INTO Employees
VALUES 
(1,'Emma Thompson',3800,1),
(2,'Daniel Rodriguez',2230,1),
(3,'Olivia Smith',2000,1),
(4,'Noah Johnson',6800,2),
(5,'Sophia Martinez',1750,1),
(8,'William Davis',6800,2),
(10,'James Anderson',4000,1) ;


CREATE TABLE Department
(
department_id INT,
department_name VARCHAR(40),
) ;

INSERT INTO Department VALUES
(1,'Data Analytics'),
(2,'Data Science');


Given a table of KPMG employee salary data, write a SQL query to find the top 3 highest paid employees in each department.

*/

-->  Answer

WITH CTE AS(
SELECT
	  	employee_id,
		name,	
		salary,
		department_id,
		ROW_NUMBER() OVER(PARTITION BY department_id ORDER BY Salary DESC) Salary_Rank
FROM Employees
)
SELECT 
		b.department_name,
		a.name as employee_name,
		a.salary
FROM CTE A
RIGHT JOIN Department B ON A.department_id=B.department_id
WHERE Salary_Rank < 4



