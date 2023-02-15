-- Lists all shows, and all genres linked to the show from the database 'hbtn_0d_tvshows'.
-- Results are ordered by ascending orderby show 'title' and genre 'name'.
SELECT t.title, g.name FROM tv_shows AS t
LEFT JOIN tv_show_genres AS s
ON t.id = s.show_id
LEFT JOIN tv_genres AS g
ON s.genre_id = g.id
ORDER BY t.title, g.name;
