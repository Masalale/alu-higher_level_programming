-- Script that lists all records of second_table with name values
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
