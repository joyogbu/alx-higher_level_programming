-- list all records contained in a database
-- mysql < hbtn_0d_tvshows.sql
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id ORDER BY tv_shows.title, tv_show_genres.genre_id ASC
