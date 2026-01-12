/*
    동물 보호소에 들어온 동물 이름 중 두 번 이상 쓰인 이름과 해당 이름이 쓰인 횟수를 조회
    - 이름이 없는 동물을 집계에서 제외 
    - 결과는 이름 순
*/

/* KEY POINT 
    1. GROUP BY col: 특정 column 기준으로 group으로 묶고, 각 group에 대해 집계 함수(COUNT, SUM, AVG 등)를 적용
    2. HAVING BY: GROUP BY 후에 group filtering (group 조건)
      WHERE: GROUP BY 전에 row를 filtering (개별 row 조건)
*/

select name, count(*)
from animal_ins
where name is not null 
group by name
having count(*) >= 2
order by name asc