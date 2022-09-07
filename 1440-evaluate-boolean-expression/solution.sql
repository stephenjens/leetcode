-- 09/07/2022 13:15	Accepted	1484 ms	0B	mysql
select
  left_operand,
  operator,
  right_operand,
  case
    when operator = '<' then if(v_l.value < v_r.value = 1, 'true', 'false')
    when operator = '>' then if(v_l.value > v_r.value = 1, 'true', 'false')
    else if(v_l.value = v_r.value, 'true', 'false')
  end as value
from
  expressions e
join
  variables v_l
on
  v_l.name = e.left_operand
join
  variables v_r
on
  v_r.name = e.right_operand;
