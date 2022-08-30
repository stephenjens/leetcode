-- 08/30/2022 09:36	Accepted	1231 ms	0B	mysql
select
  u.user_id as buyer_id,
  u.join_date,
  if(orders_in_2019 is null, 0, orders_in_2019) as orders_in_2019
from
  users u
left join (
select
  buyer_id,
  count(*) as orders_in_2019
from
  orders
where
  year(order_date) = 2019
group by
  buyer_id) t0
on
  u.user_id = t0.buyer_id;
