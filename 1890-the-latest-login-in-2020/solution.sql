-- 08/29/2022 09:13	Accepted	1673 ms	0B	mysql
select 
user_id, max(time_stamp) as last_stamp
from logins
where year(time_stamp) = '2020'
group by user_id;
