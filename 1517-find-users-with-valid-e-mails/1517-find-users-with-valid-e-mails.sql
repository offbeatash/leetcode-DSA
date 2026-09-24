/* Write your T-SQL query statement below */
SELECT user_id, name, mail
FROM Users
WHERE mail LIKE '[A-Za-z]%'
  AND mail COLLATE Latin1_General_100_BIN2 LIKE '%@leetcode.com'
  AND mail NOT LIKE '%@%@%'
  AND LEFT(mail, CHARINDEX('@leetcode.com', mail) - 1)
      NOT LIKE '%[^A-Za-z0-9_.-]%';