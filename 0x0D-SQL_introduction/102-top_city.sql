-- Import the table dump into hbtn_0c_0 database if not already imported
-- You can use the source command in the MySQL command-line:
-- SOURCE /path/to/table_dump.sql;

SELECT
    city,
    MAX(temperature) AS max_temperature
FROM
    temperatures
WHERE
    month IN (7, 8)  -- Filter for July and August
GROUP BY
    city
ORDER BY
    max_temperature DESC
LIMIT 3;
