-- 코드를 작성해주세요
select id,
case 
when ntile(4) over(order by size_of_colony desc)=1 then "CRITICAL"
when ntile(4) over(order by size_of_colony desc)=2 then "HIGH"
when ntile(4) over(order by size_of_colony desc)=3 then "MEDIUM"
ELSE "LOW"
END AS COLONY_NAME
FROM ECOLI_DATA
ORDER BY ID