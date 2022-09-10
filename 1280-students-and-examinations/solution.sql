-- 09/08/2022 15:38	Accepted	836 ms	0B	mysql
select
  st.student_id,
  st.student_name,
  su.subject_name,
  count(ex.subject_name) as attended_exams
from
  students st
cross join
  subjects su
left join
  examinations ex
on
  ex.student_id = st.student_id and
  ex.subject_name = su.subject_name
group by
  st.student_id,
  st.student_name,
  su.subject_name
order by
  st.student_id,
  su.subject_name;
