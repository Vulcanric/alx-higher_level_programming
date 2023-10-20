-- Displays records where scores are greater or equal to 10 in table `second_table`
-- Only field `score` and `name` are being displayed
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
