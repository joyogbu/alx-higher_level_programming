-- list all comedy shows in the database
SELECT tv_shows.title FROM tv_show_genres INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id WHERE tv_show_genres.genre_id = 5 ORDER BY tv_shows.title ASC
