-- 08/31/2022 08:00	Accepted	319 ms	0B	mysql
-- n.b. 'group by' is needed here
select email
from person
group by email
having count(*) > 1;
