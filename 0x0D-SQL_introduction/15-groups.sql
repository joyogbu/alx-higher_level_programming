-- select record and count by score
SELECT score, COUNT(score) As number FROM second_table GROUP BY score ORDER BY score DESC
