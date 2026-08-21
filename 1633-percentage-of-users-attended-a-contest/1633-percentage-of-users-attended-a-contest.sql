/* Write your T-SQL query statement below */
SELECT r.contest_id,
    ROUND(
        COUNT(user_id) * 100.00 /
        (SELECT COUNT(*) FROM Users u),2) AS percentage
FROM Register r
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC;