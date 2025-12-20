-- To list all records that the score is not NULL
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
