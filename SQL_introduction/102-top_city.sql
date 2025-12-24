-- To display top 3 cities based on temp across different months
SELECT city, SUM(value)/COUNT(city) AS avg_temp FROM temperatures WHERE (month = 'July' OR month = 'August') GROUP BY city ORDER BY avg_temp DESC;
