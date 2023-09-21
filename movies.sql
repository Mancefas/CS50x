-- 1.
SELECT title FROM movies WHERE year = 2008;
-- 2
SELECT birth FROM people WHERE name='Emma Stone';
-- 3
SELECT title FROM movies WHERE year >= 2018 ORDER BY title ASC;
-- 4
SELECT COUNT(rating) FROM ratings WHERE rating = 10.0;
-- 5
SELECT title,year FROM movies WHERE title LIKE 'Harry Potter%' ORDER BY year;
-- 6
SELECT AVG(rating) FROM ratings
JOIN movies ON ratings.movie_id = movies.id
WHERE year=2012;
-- 7
SELECT movies.title, ratings.rating FROM movies
JOIN ratings ON movies.id = ratings.movie_id
WHERE year = 2010
ORDER BY ratings.rating DESC, movies.title ASC;
-- 8
SELECT name FROM people 
JOIN stars ON people.id = stars.person_id 
JOIN movies ON stars.movie_id = movies.id WHERE movies.title = 'Toy Story';
-- 9
SELECT DISTINCT name
FROM people
INNER JOIN stars ON people.id = stars.person_id
INNER JOIN movies ON movies.id = stars.movie_id
WHERE movies.year = 2004
ORDER BY people.birth;
-- 10
SELECT DISTINCT people.name
FROM people
JOIN directors ON people.id = person_id
JOIN movies ON movies.id = directors.movie_id
JOIN ratings ON movies.id = ratings.movie_id
WHERE ratings.rating >= 9.0;
-- 11
SELECT movies.title FROM movies
JOIN stars ON stars.movie_id = movies.id
JOIN people ON stars.person_id = people.id
JOIN ratings ON ratings.movie_id = movies.id
WHERE people.name = 'Chadwick Boseman'
ORDER BY ratings.rating DESC
LIMIT 5;
-- 12
SELECT title FROM movies
WHERE id IN
(SELECT movie_id FROM stars JOIN people ON stars.person_id = people.id WHERE people.name = 'Bradley Cooper')
AND id IN
(SELECT movie_id FROM stars JOIN people ON stars.person_id = people.id WHERE people.name = 'Jennifer Lawrence');
-- 13
SELECT DISTINCT(people.name) FROM people
JOIN stars ON people.id = stars.person_id
JOIN movies ON stars.movie_id = movies.id
WHERE movies.title IN (SELECT DISTINCT(movies.title) FROM people
JOIN stars ON people.id = stars.person_id
JOIN movies ON stars.movie_id = movies.id
WHERE people.name = 'Kevin Bacon' AND people.birth = 1958) AND people.name != 'Kevin Bacon';