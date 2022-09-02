-- 09/02/2022 08:28	Accepted	570 ms	0B	mysql

with t0 as (
  select
    count(*) as total
  from
    delivery
)
select
  round(100 * sum(if(order_date = customer_pref_delivery_date, 1, 0)) 
    / t0.total, 2) as immediate_percentage
from
  delivery, t0;
