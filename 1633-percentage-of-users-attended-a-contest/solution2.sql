-- 09/02/2022 08:14	Accepted	1551 ms	0B	mysql

-- got this one off the discussions; it's slightly slower than mine
-- but I'm not sure if that's a legit difference, probably depends on
-- how the query optimizer does its thing
select 
  contest_id, 
  round(100 * count(*) / (select count(*) from users),2) as percentage
from
  register
group by
  contest_id
order by
  percentage desc, contest_id ;
