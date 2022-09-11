-- lol this didn't work for some reason? I think the union double-counts
with all_calls as 
(select
  caller_id, duration
from
  calls
union
select
  callee_id as caller_id, duration
from
  calls)
select
  c.name as country
from
  country c
join
  person p
on
  substring(p.phone_number, 1, 3) = c.country_code
join
  all_calls ac
on
  ac.caller_id = p.id
group by
  c.name
having
  avg(ac.duration) > (select avg(duration) from all_calls);
