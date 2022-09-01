-- 08/31/2022 08:02	Accepted	479 ms	0B	mysql
select actor_id, director_id
from actordirector
group by actor_id, director_id
having count(*) >= 3;
