/* Write your T-SQL query statement below */
WITH firstyear AS (
    SELECT
        product_id,
        MIN(year) AS first_year
    FROM Sales
    GROUP BY product_id
)

SELECT s.product_id,
    s.quantity,
    s.price,
    f.first_year
FROM Sales s
JOIN firstyear f
    ON s.product_id = f.product_id
    AND s.year = f.first_year