-- list all records contained in a table from a mysql dump
CREATE DATABASE IF NOT EXISTS hbtn_0d_tvshows;
USE hbtn_0d_tvshows;
mysql < hbtn_0d_tvshows
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows INNER JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id ORDER BY tv_shows.title, tv_show_genres.genre_id
