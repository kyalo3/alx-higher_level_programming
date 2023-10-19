-- script that displays the average temperature (Fahrenheit) by city order
SELECT
    city,
    AVG(temperature) AS avg_temperature_fahrenheit
FROM
    temperatures -- Replace with the actual table name
GROUP BY
    city
ORDER BY
    avg_temperature_fahrenheit DESC;
