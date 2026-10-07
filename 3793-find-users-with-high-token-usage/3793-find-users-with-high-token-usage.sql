/* Write your T-SQL query statement below */
SELECT
    user_id,
    COUNT(*) AS prompt_count,
    ROUND(AVG(CAST(tokens AS FLOAT)), 2) AS avg_tokens
FROM prompts
GROUP BY user_id
HAVING COUNT(*) >= 3
   AND MAX(tokens) > AVG(CAST(tokens AS FLOAT))
ORDER BY avg_tokens DESC, user_id ASC;