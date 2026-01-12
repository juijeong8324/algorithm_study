/*
    FISH_INFO 테이블에서 2021년도에 잡은 물고기 수를 출력하는 SQL 문
    - 컬럼명은 'FISH_COUNT' 
*/

/* KEY POINT
    - Like 패턴 매칭보다 Year() 가 훨씬 빠르다!
*/

-- pattern matching의 경우 
select count(*) as fish_count
from fish_info
where time like '2021%'

-- year 함수 사용(권장)
select count(*) as fish_count
from fish_info
where year(time) = 2021