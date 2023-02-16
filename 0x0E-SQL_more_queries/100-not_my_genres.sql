-- list all genres not linked to the show 'Dexter'
SELECT DISTINCT tv_genres.name FROM tv_show_genres RIGHT JOIN tv_genres on tv_genres.id=tv_show_genres.genre_id WHERE tv_genres.id NOT IN (SELECT tv_show_genres.genre_id FROM tv_show_genres WHERE tv_show_genres.show_id = 8) ORDER BY tv_genres.name ASC
