-- 08/30/2022 08:53	Accepted	399 ms	0B	mysql
-- very simple solution I found in discussions
select
  stock_name,
  sum(case when operation = 'Buy' then -1 * price else price end) as capital_gain_loss
from stocks
group by stock_name;
