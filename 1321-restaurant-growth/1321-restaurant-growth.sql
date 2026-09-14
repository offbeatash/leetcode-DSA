/* Write your T-SQL query statement below */
WITH t AS (
    SELECT visited_on, SUM(amount) amount
    FROM Customer
    GROUP BY visited_on
)
SELECT visited_on,
       SUM(amount) OVER (ORDER BY visited_on ROWS 6 PRECEDING) amount,
       ROUND(SUM(amount) OVER (ORDER BY visited_on ROWS 6 PRECEDING) / 7.0, 2) average_amount
FROM t
ORDER BY visited_on
OFFSET 6 ROWS;