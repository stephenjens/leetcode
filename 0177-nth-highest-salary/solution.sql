-- 08/27/2022 12:52	Accepted	293 ms	0B	mysql
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  set n = n - 1;
  RETURN (
      -- outside select will return null if inside select is empty
      select(select distinct salary from employee order by salary desc limit 1 offset n)
  );
END
