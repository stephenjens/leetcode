-- 09/01/2022 08:24	Accepted	779 ms	0B	mysql
select 
  u.product_id, 
  round(sum(p.price * u.units) / sum(u.units), 2) as average_price
from
  unitssold u
left join
  prices p
on 
  p.product_id = u.product_id and
  u.purchase_date between p.start_date and p.end_date
group by u.product_id;
