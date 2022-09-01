-- 08/31/2022 08:33	Accepted	1166 ms	0B	mysql
-- this one is faster because it doesn't do as many date comparisons? I dunno
select p.product_id, p.product_name
from product p
join (
  select
      product_id, count(*)
  from 
      sales
  group by 
      product_id
  having
      max(sale_date) <= '2019-03-31' and min(sale_date) >= '2019-01-01'
) t0
on p.product_id = t0.product_id;
