-- 09/03/2022 08:55	Accepted	912 ms	0B	mysql

-- simpler version of solution.sql without the inner query
select
  seller_name
from
  seller s
left join 
  orders o
on
  o.seller_id = s.seller_id and
  year(o.sale_date) = 2020
where
  o.seller_id is NULL
order by
  seller_name asc;
