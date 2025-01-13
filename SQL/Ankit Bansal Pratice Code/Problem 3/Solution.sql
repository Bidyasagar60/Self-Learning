

SELECT * FROM Hospital;
 
--> Apprach 1:

WITH CTE AS
(
SELECT
		Emp_Id,
	    Action,
		Time,
		ROW_NUMBER() OVER(PARTITION BY emp_id ORDER BY time DESC) RN

FROM Hospital)
SELECT 
		COUNT(*) AS [Person in Hospital]

FROM CTE 
WHERE RN=1
AND Action='in'

--> Approach 2:


SELECT 
		COUNT(*)  AS [Person in Hospital]

FROM Hospital A
INNER JOIN (SELECT 
					Emp_ID,
					MAX(Time) MaxTime
			FROM Hospital
			GROUP BY Emp_Id ) B ON A.Emp_Id=B.Emp_ID and A.TIme=B.MaxTime

WHERE A.Action='in'
