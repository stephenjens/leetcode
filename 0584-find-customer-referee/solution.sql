-- 08/22/2022 10:18	Accepted	446 ms	0B	mysql
select name from Customer where (referee_id is null or referee_id <> 2);
