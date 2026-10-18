/* Write your T-SQL query statement below */
SELECT request_at AS Day,
    ROUND(AVG(CASE 
        WHEN status = 'completed' THEN 0.0 ELSE 1.0 END), 2) AS [Cancellation Rate]
FROM Trips t
JOIN Users u 
    ON t.client_id = u.users_id AND u.banned = 'NO'
JOIN Users v 
    ON t.driver_id = v.users_id AND v.banned = 'NO'
WHERE request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY request_at;