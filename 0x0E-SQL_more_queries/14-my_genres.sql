-- list all genres of yhe show Dexter
SELECT tv_genres.name FROM tv_show_genres INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id WHERE tv_show_genres.show_id = 8 ORDER BY tv_genres.name ASC
