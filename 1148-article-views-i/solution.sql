-- 08/26/2022 13:50	Accepted	350 ms	0B	mysql
select distinct author_id as id
from views v0
where author_id = viewer_id
order by id;
