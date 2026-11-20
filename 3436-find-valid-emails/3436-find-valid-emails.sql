SELECT
    user_id,
    email
FROM Users
WHERE
    email LIKE '%.com'
    AND LEN(email) - LEN(REPLACE(email, '@', '')) = 1
    AND CHARINDEX('@', email) > 1
    AND LEFT(email, CHARINDEX('@', email) - 1) NOT LIKE '%[^0-9A-Za-z_]%'
    AND LEN(email) - CHARINDEX('@', email) - 4 > 0
    AND SUBSTRING(
            email,
            CHARINDEX('@', email) + 1,
            LEN(email) - CHARINDEX('@', email) - 4
        ) NOT LIKE '%[^A-Za-z]%'
ORDER BY user_id;