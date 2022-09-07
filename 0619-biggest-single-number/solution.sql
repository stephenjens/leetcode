-- 09/07/2022 09:58	Accepted	629 ms	0B	mysql
select (
  select 
    num
  from
    mynumbers
  group by num
  having count(*) = 1
  order by num desc
  limit 1) 
as 
  num
from
  dual;
