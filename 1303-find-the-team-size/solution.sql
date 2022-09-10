-- 09/08/2022 15:14	Accepted	601 ms	0B	mysql
select
  e1.employee_id, count(*) as team_size
from
  employee e0
left join
  employee e1
on
  e1.team_id = e0.team_id
group by
  e1.employee_id;
