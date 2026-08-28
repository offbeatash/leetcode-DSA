/* Write your T-SQL query statement below */
SELECT
    activity_date AS day,
    COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date >= '20190628'
  AND activity_date < '20190728'
GROUP BY activity_date;