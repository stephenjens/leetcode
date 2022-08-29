-- from solution tab
-- 08/29/2022 08:57	Accepted	758 ms	0B	mysql
select customer_number
from orders
group by customer_number
order by count(*) desc
limit 1;
