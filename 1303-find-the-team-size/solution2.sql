-- 09/08/2022 15:18	Accepted	537 ms	0B	mysql
-- suggestion using windowing from discussion
select
  employee_id,
  count(team_id) over (partition by team_id) as team_size
from
  employee;
