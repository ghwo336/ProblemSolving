-- 코드를 입력하세요
SELECT USER_ID,PRODUCT_ID
FROM ONLINE_SALE
Group by user_id,product_id
having count(*)>=2
order by user_id,product_id desc