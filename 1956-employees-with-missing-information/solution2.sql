-- 08/25/2022 12:29	Accepted	479 ms	0B	mysql
select distinct bob as employee_id from
(select e.employee_id as bob from employees e union select s.employee_id as bob from salaries s
) t0
left join employees e on e.employee_id = t0.bob
left join salaries s on s.employee_id = t0.bob
where e.name is null or s.salary is null order by employee_id;
