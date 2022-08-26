-- 08/26/2022 13:36	Accepted	314 ms	0B	mysql
-- i already did this one 4 days ago with the same solution and somehow it's
-- twice as fast this time
select p.firstname, p.lastname, a.city, a.state
from person p
left join address a on p.personid = a.personid;
