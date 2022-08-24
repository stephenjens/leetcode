-- 08/24/2022 11:08	Accepted	552 ms	0B	mysql
select patient_id, patient_name, conditions
from patients
where regexp_like(conditions, '(^| )DIAB1.*');
