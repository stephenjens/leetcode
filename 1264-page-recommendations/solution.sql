-- 09/07/2022 14:34	Accepted	595 ms	0B	mysql
select
  distinct page_id as recommended_page
from
  likes
join
  friendship
on
  (user1_id = 1 and user2_id = user_id) or
  (user2_id = 1 and user1_id = user_id)
where
  page_id
not in
  (select page_id from likes where user_id = 1);
