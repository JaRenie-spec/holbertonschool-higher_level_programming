-- List all cities of California sorted by cities.id in ascending order without using JOIN
SELECT id, name
FROM cities
WHERE state_id = (
	SELECT id
	FROM states
	WHERE name = 'California')
ORDER BY id ASC;
