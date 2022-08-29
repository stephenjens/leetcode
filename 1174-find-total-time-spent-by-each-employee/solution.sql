-- 08/29/2022 09:16	Accepted	401 ms	0B	mysql
select
    event_day as day,
    emp_id,
    sum(out_time - in_time) as total_time
from
    employees
group by
    day, emp_id;
