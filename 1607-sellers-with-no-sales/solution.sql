-- 09/03/2022 08:48	Accepted	970 ms	0B	mysql
select
  seller_name
from
  seller s
left join (
select
  seller_id,
  count(*) as total_orders
from
  orders
where
  year(sale_date) = 2020
group by
  seller_id
) t0
on
  s.seller_id = t0.seller_id
where
  total_orders is NULL
order by
  seller_name asc;
