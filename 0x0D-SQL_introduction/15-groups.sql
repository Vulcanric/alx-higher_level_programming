-- Lists the number of records with the same score along with the score
-- in the table `second_table`
SELECT DISTINCT score, COUNT(score) AS number FROM second_table GROUP BY score;
