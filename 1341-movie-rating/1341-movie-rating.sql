/* Write your T-SQL query statement below */
SELECT results
FROM
(
    SELECT TOP 1
        u.name AS results,
        1 AS sort_order
    FROM Users u
    JOIN MovieRating mr
        ON u.user_id = mr.user_id
    GROUP BY u.user_id, u.name
    ORDER BY COUNT(*) DESC, u.name ASC
) AS A

UNION ALL

SELECT results
FROM
(
    SELECT TOP 1
        m.title AS results,
        2 AS sort_order
    FROM Movies m
    JOIN MovieRating mr
        ON m.movie_id = mr.movie_id
    WHERE mr.created_at >= '2020-02-01'
      AND mr.created_at < '2020-03-01'
    GROUP BY m.movie_id, m.title
    ORDER BY AVG(CAST(mr.rating AS DECIMAL(10,2))) DESC,
             m.title ASC
) AS B;