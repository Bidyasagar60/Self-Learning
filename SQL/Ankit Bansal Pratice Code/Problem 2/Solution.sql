
WITH CTE AS (

SELECT
		*,
		DATEDIFF(Day,create_Date,resolved_date) -( DATEDIFF(WEEK,create_Date,resolved_date) *2) AS Diff

FROM tickets
)
SELECT 
		A.ticket_id,
		A.create_date,
		A.resolved_date,
		diff,
		A.Diff - (SELECT COUNT(*) FROM holidays B 
				  WHERE B.holiday_date BETWEEN A.create_date 
				  AND A.resolved_date AND DATEPART(WEEKDAY,holiday_date) NOT IN (1,7)) AS business_days


FROM CTE A

