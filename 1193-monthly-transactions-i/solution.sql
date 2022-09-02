-- 09/02/2022 08:06	Accepted	920 ms	0B	mysql

select 
  date_format(trans_date, '%Y-%m') as month,
  country as country,
  count(*) as trans_count,
  sum(if(state = 'approved', 1, 0)) as approved_count,
  sum(amount) as trans_total_amount,
  sum(if(state = 'approved', amount, 0)) as approved_total_amount
from
  transactions
group by month, country;
