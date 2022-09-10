-- 08/27/2022 13:13	Accepted	773 ms	0B	mysql

-- had to look up window frame specification syntax for this one: "A
-- frame is a subset of the current partition and the frame clause
-- specifies how to define the subset. "
select player_id, event_date, sum(games_played) over w as games_played_so_far
from activity
window w as (partition by player_id order by event_date rows unbounded preceding);
