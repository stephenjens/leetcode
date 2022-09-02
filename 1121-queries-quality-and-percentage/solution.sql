-- 09/02/2022 08:38	Accepted	583 ms	0B	mysql
select
  query_name,
  round(avg(rating / position), 2) as quality,
  round(100 * sum(if(rating < 3, 1, 0)) / count(*), 2) as poor_query_percentage
from
  queries
group by query_name;
