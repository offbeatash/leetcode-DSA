/* Write your T-SQL query statement below */
SELECT DISTINCT customer_id
FROM Customer c
JOIN Product p
ON c.product_key = p.product_key
GROUP BY customer_id
HAVING COUNT(DISTINCT p.product_key) = (
    SELECT COUNT(*) FROM Product
);