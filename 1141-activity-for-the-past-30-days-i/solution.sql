-- 08/28/2022 16:41	Accepted	505 ms	0B	mysql
-- I subtracted 29 days as the problem asked for "period of 30 days ending '2019-07-27'"
select activity_date as day, count(*) as active_users
from
(
    select distinct user_id, activity_date
    from activity
    where activity_date between date_sub('2019-07-27', interval 29 day) and '2019-07-27'
) t0
group by day;
