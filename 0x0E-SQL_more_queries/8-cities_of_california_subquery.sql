-- Lists all cities of Califonia that can be found in the database 'hbtn_0d_usa'.
-- Results are ordered by ascending order by 'cities.id'
SELECT id, name FROM cities
 WHERE state_id =
       (SELECT id
	  FROM states
	 WHERE name = "California")
 ORDER BY id;
