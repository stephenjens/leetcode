-- 08/24/2022 14:31	Accepted	614 ms	0B	mysql
select distinct player_id, first_value(event_date) over w as 'first_login'
from activity
window w as (partition by player_id order by event_date);
