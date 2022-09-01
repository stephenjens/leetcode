-- 09/01/2022 08:38	Accepted	374 ms	0B	mysql
select
  sale_date,
  sum(if(fruit = 'apples', sold_num, -1 * sold_num)) as diff
from
  sales
group by sale_date
order by sale_date;
