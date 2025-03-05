-- 코드를 입력하세요
SELECT rr.rest_id,ri.rest_name,ri.food_type,ri.favorites,ri.address,round(avg(rr.review_score),2) as score
from rest_info as ri
join rest_review as rr
on ri.rest_id=rr.rest_id
group by rr.rest_id having ri.address like "서울%"
order by score desc,ri.favorites desc;