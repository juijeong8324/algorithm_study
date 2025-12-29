/*
    잡은 물고기의 평균 길이를 출력하는 SQL문을 작성
    - 평균 길이를 나타내는 컬럼 명은 AVERAGE_LENGTH
    - 평균 길이는 소수점 3째자리에서 반올림
    - 10cm 이하의 물고기들은 10cm 로 취급하여 평균 길이를 구해라 
*/

/* KEY POINT
    1. WHERE 절은 조건이 필요하다. 따라서 where 절에는 비교 연산자가 필요하다. 
    2. 따라서 coalesce 함수(null 값이 아닌 값을 먼저 return)는 select 절, 특히 avg 함수 안에서 수행되어야 한다.
*/
select round(avg(coalesce(length, 10)), 2) as average_length
from fish_info