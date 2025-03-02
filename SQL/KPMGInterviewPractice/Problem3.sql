
/*

CREATE TABLE Projects
(
project_id  INT,
client_name  VARCHAR(30),
project_name VARCHAR(30)
)


INSERT INTO Projects
VALUES (100,'Apple','Market Analysis'),
(101,'Google','Competitive Research'),
(102,'Microsoft','Business Strategy')


CREATE TABLE Tasks
(
task_id INT,
project_id INT,
employee_id INT,
hours_billed INT)

INSERT INTO Tasks VALUES
(500,100,123,10),
(501,101,265,8),
(502,101,362,6),
(503,102,192,9),
(504,102,981,11)



KPMG as a consulting firm executes various projects for different clients. Each project often consists of multiple tasks and 
each task is assigned to one or more employees, where each employee can log the hours they've worked. For this question, 
we're interested in the average number of hours billed per project. Write a SQL query which calculates the average hours billed to each project.

*/


WITH CTE AS(
SELECT 
	  Project_id,
	  AVG(hours_billed) Avg_Hours_Billed
FROM tasks
GROUP BY Project_id)

SELECT 
		B.Project_id,
		B.project_name,
		A.Avg_Hours_Billed
FROM CTE A
RIGHT JOIN Projects B ON A.Project_id=B.Project_id