-- 08/22/2022 12:00	Accepted	466 ms	0B	mysql
select player_id, event_date as first_login from (
select player_id, event_date, dense_rank() over ( partition by player_id order by event_date asc) dr
from activity
    ) t where t.dr = 1;
