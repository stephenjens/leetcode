-- 09/08/2022 15:03	Accepted	464 ms	0B	mysql
select
  e0.name
from
  employee e0
right join
  employee e1
on
  e0.id = e1.managerId
group by
  e0.name
having
  count(*) >= 5 and e0.name is not null;
