-- To list all genres and the number of links
SELECT tv_genres.name AS genre, COUNT(tv_shows.title) AS number_of_shows
FROM tv_show_genres
INNER JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
INNER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
ORDER BY number_of_shows DESC
GROUP BY genre;
