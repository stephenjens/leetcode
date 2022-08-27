-- 08/27/2022 11:23	Accepted	526 ms	0B	mysql
-- solution from leetcode; almost did it this way myself but joined on
-- id instead of what's here
select w1.id from weather w1
join weather w0
on datediff(w1.recordDate, w0.recordDate) = 1 and w1.temperature > w0.temperature;
