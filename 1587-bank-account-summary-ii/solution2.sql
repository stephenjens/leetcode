-- 08/31/2022 08:09	Accepted	644 ms	0B	mysql
-- do the summing of amounts before the join for a small speedup
gselect u.name, t0.balance
from users u
join
  (
    select account, sum(amount) as balance
    from transactions
    group by account
  ) t0
on u.account = t0.account
where balance > 10000;
