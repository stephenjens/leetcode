-- 08/27/2022 11:48	Accepted	833 ms	0B	mysql

select e0.name as employee
from employee e0
join employee e1 on e0.managerid = e1.id and e0.salary > e1.salary;
