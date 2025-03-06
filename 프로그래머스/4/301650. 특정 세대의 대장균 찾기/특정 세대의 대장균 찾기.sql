-- 코드를 작성해주세요
select a.id
from ecoli_data as a, ecoli_data as b, ecoli_data as c
where a.parent_id=b.id and b.parent_id=c.id and c.parent_id is null