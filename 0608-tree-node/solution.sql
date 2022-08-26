-- 08/25/2022 14:13	Accepted	782 ms	0B	mysql
-- this one...stumped...me a bit
select id,
case
  when p_id is null then 'Root'
  when id in (select p_id from tree) then 'Inner'
  else 'Leaf'
end as type 
from tree
order by id;
