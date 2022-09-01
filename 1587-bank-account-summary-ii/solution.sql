-- 08/31/2022 08:07	Accepted	910 ms	0B	mysql
select u.name, sum(t.amount) as balance
from users u, transactions t
where u.account = t.account
group by u.name
having balance > 10000;
