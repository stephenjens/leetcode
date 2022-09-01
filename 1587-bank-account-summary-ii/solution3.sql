-- 08/31/2022 08:13	Accepted	1516 ms	0B	mysql
-- i thought filtering before the join would be faster but it's not in this case
select u.name, t0.balance
from users u
join
  (
    select account, sum(amount) as balance
    from transactions
    group by account
    having balance > 10000
  ) t0
on u.account = t0.account;
