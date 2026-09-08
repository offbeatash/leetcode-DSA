/* Write your T-SQL query statement below */
SELECT product_id,
       ISNULL(
           (SELECT TOP 1 new_price
            FROM Products q
            WHERE q.product_id = p.product_id
              AND change_date <= '2019-08-16'
            ORDER BY change_date DESC), 10) AS price
FROM Products p
GROUP BY product_id
ORDER BY product_id;