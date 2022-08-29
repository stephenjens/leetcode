-- 08/29/2022 08:53	Accepted	511 ms	0B	mysql
select customer_number from (
    select customer_number, count(*) as order_count
    from orders
    group by customer_number order by order_count desc
) t0 limit 1;
