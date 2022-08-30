-- 08/30/2022 09:10	Accepted	909 ms	0B	mysql
select name, travelled_distance
from (
select
    u.id,
    u.name, 
    sum(case when r.distance is null then 0 else r.distance end) as travelled_distance
from
    users u
left join
    rides r
on
    u.id = r.user_id
group by u.id, u.name) t0
order by travelled_distance desc, name asc;
