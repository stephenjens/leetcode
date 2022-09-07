-- 09/07/2022 12:58	Accepted	668 ms	0B	mysql

select customer_id, customer_name
from (
  select
    c.customer_id, c.customer_name, group_concat(distinct product_name order by product_name) as products
  from
    customers c
  join
    orders o
  on 
    c.customer_id = o.customer_id
  group by
    c.customer_id, c.customer_name
  having
    products like 'A,B%' and
    products not like 'A,B,C%'
) t0;
