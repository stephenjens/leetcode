-- 09/07/2022 10:12	Accepted	754 ms	0B	mysql
select
  distinct student_id,
  first_value(course_id)  over w as course_id,
  first_value(grade)  over w as grade
from enrollments
window w as (partition by student_id order by grade desc, course_id asc);
