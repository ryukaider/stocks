select * from api_progress
order by daily_history asc

select * from company_profile
where sector = ''
and industry = 'Textiles'

select distinct sector from company_profile

select distinct industry from company_profile
where sector = 'Commercial Services'
