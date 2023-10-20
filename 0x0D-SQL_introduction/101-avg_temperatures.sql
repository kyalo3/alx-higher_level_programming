-- displays the average temperature by city order
SELECT city, AVG(value) AS avg_temperature FROM 'temperatures' GROUP BY city ORDER BY avg_temperature DESC;
