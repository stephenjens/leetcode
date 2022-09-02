-- 09/02/2022 08:30	Accepted	822 ms	0B	mysql

-- moving 'count(*) from delivery' out of a 'with ...' statement and
-- into the may query was much slower this time
select
  round(100 * sum(if(order_date = customer_pref_delivery_date, 1, 0)) 
    / (select count(*) from delivery), 2) as immediate_percentage
from
  delivery;
