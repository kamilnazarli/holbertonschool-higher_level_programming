-- To find average temperature for each city
SELECT city, SUM(value)/COUNT(city) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp;
