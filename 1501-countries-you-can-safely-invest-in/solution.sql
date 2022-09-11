-- 09/11/2022 11:55	Accepted	1319 ms	0B	mysql
-- lifted from discussion
select
  co.name as country
from
  country co
join
  person p
on
  substring(p.phone_number, 1, 3) = co.country_code
join
  calls ca
on
  p.id in (ca.caller_id, ca.callee_id)
group by
  co.name
having
  avg(ca.duration) > (select avg(duration) from calls)
