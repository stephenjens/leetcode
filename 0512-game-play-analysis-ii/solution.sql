-- 08/27/2022 13:04	Accepted	649 ms	0B	mysql

select distinct player_id, first_value(device_id) over w as device_id
from activity
window w as (partition by player_id order by event_date);
