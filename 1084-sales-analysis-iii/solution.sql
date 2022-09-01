-- 08/31/2022 08:29	Accepted	1467 ms	0B	mysql
select p.product_id, p.product_name
from product p
join (
selectnn
    product_id,
    sum(if(sale_date between '2019-01-01' and '2019-03-31', 1, 0)) as q1_2019,
    sum(if(sale_date not between '2019-01-01' and '2019-03-31', 1, 0)) as not_q1_2019
from sales
group by product_id
) t0
on p.product_id = t0.product_id and q1_2019 > 0 and not_q1_2019 = 0;
