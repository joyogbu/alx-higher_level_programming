-- lisall records contained in a database
-- mysql < hbtn_0d_tvshows.sql
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_show_genres RIGHT JOIN tv_shows ON tv_shows.id=tv_show_genres.show_id WHERE tv_show_genres.genre_id IS NULL ORDER BY tv_shows.title, tv_show_genres.genre_id ASC
