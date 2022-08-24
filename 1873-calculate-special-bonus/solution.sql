-- 08/23/2022 10:11	Accepted	1595 ms	0B	mysql
select employee_id,
case when employee_id % 2 = 1 and name not like 'M%' then salary else 0 end as bonus
from employees order by employee_id;
