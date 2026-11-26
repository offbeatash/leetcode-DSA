/* Write your T-SQL query statement below */
SELECT customer_id
from customer_transactions
group by customer_id
having
    sum(case 
            when transaction_type = 'purchase' then 1 else 0 end) >=3

    and datediff(
        day, min(transaction_date), max(transaction_date)
    ) >= 30

    and sum(case
                when transaction_type = 'refund' then 1 else 0 end) * 1.0 / count(*) < 0.20
order by customer_id