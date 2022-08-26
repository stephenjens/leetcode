-- 08/25/2022 12:09	Accepted	1545 ms	0B	mysql
select employee_id from (
  select e.employee_id, e.name, s.salary from employees e
  left join salaries s on s.employee_id = e.employee_id
    union
  select s.employee_id, e.name, s.salary from salaries s
  left join employees e on e.employee_id = s.employee_id
) t
where t.name is null or t.salary is null order by employee_id;
