-- 09/01/2022 08:29	Accepted	693 ms	0B	mysql
select
  w.name as warehouse_name,
  sum(w.units * p.width * p.length * p.height) as volume
from
  warehouse w
left join
  products p
on
  w.product_id = p.product_id
group by warehouse_name;
