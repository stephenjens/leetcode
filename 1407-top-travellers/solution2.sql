-- 08/30/2022 09:14	Accepted	768 ms	0B	mysql

-- maybe faster than solution.sql? this one summarizes the rides table
-- before joining with users instead of doing. this seems like it
-- would be faster if many users had multiple rides.

-- also I believe the if(...) is mysql-specific, a more generic
-- version would use a case statement
select
  u.name,
  if(travelled_distance is null, 0, travelled_distance) as travelled_distance
from
  users u
left join
(select
  user_id, sum(distance) as travelled_distance
from
  rides
group by user_id) t0
on
  u.id = t0.user_id
order by travelled_distance desc, name asc;
