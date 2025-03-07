-- 코드를 입력하세요
select distinct(car_id),ch.car_type,floor(ch.fee*(100-plan.discount_rate)/100) as fee
from 
(
SELECT  distinct(car.car_id),car.car_type,car.daily_fee*30 as fee
from car_rental_company_car as car
right
join 
(
    select distinct car_id
    from car_rental_company_rental_history
    where car_id not in(
    select distinct car_id
        from car_rental_company_rental_history
        where end_date>="2022-11-01" and start_date<="2022-11-30"
    )

)    
    
    
as history
on car.car_id=history.car_id
where (car.car_type="SUV" or car.car_type="세단")
) as ch
join car_rental_company_discount_plan as plan
on ch.car_type=plan.car_type
where plan.duration_type="30일 이상" and fee>=500000 and fee<2000000
order by fee desc,car_type asc,car_id desc;