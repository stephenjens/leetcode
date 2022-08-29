-- 08/28/2022 16:55	Accepted	479 ms	0B	mysql
select user_id, count(*) as followers_count
from followers
group by user_id order by user_id;
