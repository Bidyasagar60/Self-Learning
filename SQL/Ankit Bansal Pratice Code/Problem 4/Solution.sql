
SELECT 
		Value as Room_Type,
		COUNT(*) Searched
FROM AirBnb_Searches
CROSS APPLY  string_split(filter_room_types,',') AS FilterType
GROUP BY Value
ORDER BY Searched DESC 