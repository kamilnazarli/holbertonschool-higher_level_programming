-- To list all cities contained in a database
SELECT cities.id, cities.name, states.name
FROM states
INNER JOIN cities
ON cities.id = states.id
ORDER BY cities.id;
