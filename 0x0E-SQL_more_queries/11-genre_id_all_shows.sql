-- Lists all shows contained in the database 'hbtn_0d_tvshows'.
-- If show doesn't have a genre, display 'NULL'
-- Results are ordered by ascending order, 'tv_shows.title' and 'tv_show_genres.genre_id'.
SELECT s.title, g.genre_id FROM tv_shows AS s
LEFT JOIN tv_show_genres AS g
ON s.id = g.show_id
ORDER BY s.title, g.genre_id;
