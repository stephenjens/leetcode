-- 08/27/2022 11:39	Accepted	2235 ms	0B	mysql

select distinct sp.name
from salesperson sp
-- left join to include salespersons without orders
left join orders o on o.sales_id = sp.sales_id 
where sp.sales_id not in ( 
    select sales_id from orders, company
    where orders.com_id = company.com_id and company.name = 'RED');
