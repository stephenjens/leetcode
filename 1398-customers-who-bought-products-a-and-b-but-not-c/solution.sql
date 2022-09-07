-- 09/07/2022 12:55	Accepted	1639 ms	0B	mysql
select
  c.customer_id, c.customer_name
from
  customers c
join (
select
  customer_id, group_concat(distinct product_name order by product_name) as products
from
  orders
group by 
  customer_id
having
  products like 'A,B%' and
  products not like 'A,B,C%'
) t0
on 
  t0.customer_id = c.customer_id
order by 
  c.customer_id;
