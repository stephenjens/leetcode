-- 08/29/2022 09:02	Accepted	500 ms	0B	mysql
-- this also works
select distinct 
player_id,
first_value(event_date) over (partition by player_id order by event_date) as first_login
from activity;
