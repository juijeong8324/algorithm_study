/*
    CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블에서 대여 시작일이 2022년 9월에 속하는 대여 기록을 출력하는 SQL문을 작성
    - 대여 기간이 30일 이상이면 '장기 대여' 그렇지 않으면 '단기 대여' 로 표시하는 컬럼(컬럼명: RENT_TYPE)을 추가
    - 결과는 대여 기록 ID를 기준으로 내림차순 정렬
*/

/*  KEY POINT 
    1. Date type의 경우, 두 날짜의 간격을 구하고 싶으면 DATEDIFF(date1, date2) 를 사용하자. 
        - date1-date2 를 하면 10진법 뺄셈이 되어 잘못된 값을 얻는다.
*/

select history_id, car_id, 
        date_format(start_date, '%Y-%m-%d') as start_date, 
        date_format(end_date, '%Y-%m-%d') as end_date,
        case when datediff(end_date, start_date)+1 >= 30 
        then '장기 대여' 
        else '단기 대여' 
        end as rent_type
from car_rental_company_rental_history
where year(start_date) = 2022 and month(start_date) = 9 
order by history_id desc