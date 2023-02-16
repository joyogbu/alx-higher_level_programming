-- list and count the number of records in a database
SELECT name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows FROM tv_show_genres INNER JOIN tv_genres ON tv_genres.id=tv_show_genres.genre_id GROUP BY name ORDER BY number_of_shows DESC
