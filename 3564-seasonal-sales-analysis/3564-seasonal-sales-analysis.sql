WITH x AS (
    SELECT
        CASE WHEN MONTH(sale_date) IN (12,1,2) THEN 'Winter'
             WHEN MONTH(sale_date) IN (3,4,5) THEN 'Spring'
             WHEN MONTH(sale_date) IN (6,7,8) THEN 'Summer'
             ELSE 'Fall' END season,
        category,
        SUM(quantity) total_quantity,
        SUM(quantity * price) total_revenue
    FROM Sales s JOIN Products p ON s.product_id = p.product_id
    GROUP BY
        CASE WHEN MONTH(sale_date) IN (12,1,2) THEN 'Winter'
             WHEN MONTH(sale_date) IN (3,4,5) THEN 'Spring'
             WHEN MONTH(sale_date) IN (6,7,8) THEN 'Summer'
             ELSE 'Fall' END, category
),
r AS (
    SELECT *, ROW_NUMBER() OVER(
        PARTITION BY season
        ORDER BY total_quantity DESC, total_revenue DESC, category
    ) n
    FROM x
)
SELECT season, category, total_quantity, total_revenue
FROM r WHERE n = 1;