-- 08/25/2022 14:33	Accepted	199 ms	0B	mysql
select if(count(salary) > 0, salary, null) as SecondHighestSalary from (
    select distinct salary from employee order by salary desc limit 1 offset 1
) t0;
