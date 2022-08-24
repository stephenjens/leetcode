-- 08/23/2022 10:44	Accepted	851 ms	0B	mysql
-- solution not mine (this one stumped me)
delete p1 from person p1, person p2 where p1.email = p2.email and p1.id > p2.id;
