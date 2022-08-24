-- 08/22/2022 09:58	Accepted	789 ms	0B	mysql
select p.firstName, p.lastName, a.city, a.state from
Person p left join Address a on (p.personId = a.personId);
