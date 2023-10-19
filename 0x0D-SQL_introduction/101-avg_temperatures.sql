-- script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
SELECT
    city,
    AVG(temperature) AS avg_temperature_fahrenheit
FROM
    your_table_name -- Replace with the actual table name
GROUP BY
    city
ORDER BY
    avg_temperature_fahrenheit DESC;
