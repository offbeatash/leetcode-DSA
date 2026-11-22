/* Write your T-SQL query statement below */

WITH CTE AS
(
    select distinct 
        p.user_id,
        i.category
    FROM ProductPurchases p
    JOIN ProductInfo i
        ON p.product_id = i.product_id
)
SELECT
    A.category as category1,
    B.category as category2,
    COUNT(*) AS customer_count
FROM CTE A
JOIN CTE B
    ON A.user_id = B.user_id
    AND A.category < B.category
GROUP BY A.category, B.category
HAVING COUNT(*) >= 3
ORDER BY customer_count DESC, category1, category2