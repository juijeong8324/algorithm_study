/*
    CAR_RENTAL_COMPANY_CAR 테이블에서 '네비게이션' 옵션이 포함된 자동차 리스트를 출력하는 SQL문을 작성 
    - 자동차 ID를 기준으로 내림차순 정렬해주세요.
*/

/* KEY POINT
    1. options은 문자열로 이루어져 있기 떄문에 특정 패턴이 있는지 확인하려면 'LIKE' 키워드를 사용해야 함 
    2. %의 의미는 0개 이상의 문자를 의미함
*/

select *
from CAR_RENTAL_COMPANY_CAR
where options like '%네비게이션%'
order by car_id desc