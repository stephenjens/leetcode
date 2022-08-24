-- 08/24/2022 11:03	Accepted	430 ms	0B	mysql
-- 08/24/2022 11:01	Accepted	635 ms	0B	mysql

-- this solution I found in comments section; my original solution worked but was way more complicated lol
select sell_date,
count(distinct(product)) as num_sold,
group_concat(distinct product order by product separator ',') as products
from activities
group by sell_date
order by sell_date;
