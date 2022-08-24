-- 08/24/2022 10:57	Accepted	737 ms	0B	mysql
select user_id,
concat(ucase(substr(name, 1, 1)), lcase(substr(name, 2))) as name
from users order by user_id;
