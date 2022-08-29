-- 08/28/2022 16:50	Accepted	670 ms	0B	mysql
select date_id, make_name, 
  count(distinct(lead_id)) as unique_leads,
  count(distinct(partner_id)) as unique_partners
from dailysales
group by date_id, make_name;
