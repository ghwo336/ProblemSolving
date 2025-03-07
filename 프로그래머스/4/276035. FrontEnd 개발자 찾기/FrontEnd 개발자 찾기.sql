-- 코드를 작성해주세요
select distinct(d.id),d.email,d.first_name,d.last_name
from developers as d
join skillcodes as s
on d.skill_code&s.code=s.code
where s.category="Front End"
order by d.id asc;