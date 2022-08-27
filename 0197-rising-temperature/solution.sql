-- 08/27/2022 11:19	Accepted	761 ms	0B	mysql

-- window function worked well but I had to look up lag() and
-- datediff() (oracle uses date_1 - date_2, no extra function needed);
-- learned that 'window w as (...)' doesn't need 'partition by'
select id from (
  select id, 
  datediff(recordDate, lag(recordDate, 1) over w) as datelag,
  temperature,
  lag(temperature, 1) over w as prev
  from weather
  window w as (order by recordDate)
) t0 where temperature > prev and datelag = 1;
