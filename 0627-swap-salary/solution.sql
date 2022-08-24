-- 08/23/2022 10:16	Accepted	363 ms	0B	mysql
update salary set sex = (case when sex = 'm' then 'f' else 'm' end);
