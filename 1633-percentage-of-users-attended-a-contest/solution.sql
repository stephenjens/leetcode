-- 09/02/2022 08:12	Accepted	1518 ms	0B	mysql
with t0 as (
  select
    count(*) as total_users
  from users
)
select
  contest_id,
  round(100 * count(*) / t0.total_users, 2) as percentage
from
  register, t0
group by
  contest_id
order by percentage desc, contest_id asc;
