/* Write your T-SQL query statement below */
SELECT s.name
FROM Salesperson s
WHERE s.sales_id NOT IN (
    SELECT o.sales_id
    FROM Orders o
    JOIN Company c
        ON c.com_id = o.com_id
    WHERE c.name = 'RED'
)