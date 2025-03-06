-- 코드를 작성해주세요

select id,count(b.parent_id)as child_count
from ecoli_data as a
left
join (
select parent_id
    from ecoli_data
) as b
on  a.id=b.parent_id
group by id

