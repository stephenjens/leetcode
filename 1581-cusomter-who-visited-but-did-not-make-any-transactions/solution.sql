-- 08/26/2022 13:46	Accepted	1360 ms	0B	mysql
select v.customer_id, count(*) as count_no_trans
from visits v
left join transactions t on v.visit_id = t.visit_id
where t.transaction_id is null
group by v.customer_id;
