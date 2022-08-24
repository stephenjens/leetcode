-- 08/22/2022 10:32	Accepted	418 ms	0B	mysql
select c.name as 'Customers'
from Customers c
where c.id not in (select customerId from Orders);

-- my original solution:
-- select name Customers from (
-- select c.name, order_count from Customers c
-- left join (select o.customerId, count(*) order_count from Orders o group by
-- customerId) t
-- on c.id = t.customerId) s
-- where order_count is null;

