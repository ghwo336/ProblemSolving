-- 코드를 작성해주세요

select fi.id,fni.fish_name,fi.length
from fish_info as fi
join fish_name_info as fni
on fi.fish_type=fni.fish_type
where fi.length=(
select max(length)
    from fish_info
    where fish_type=fi.fish_type
)
