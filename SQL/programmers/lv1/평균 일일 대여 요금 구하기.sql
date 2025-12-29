/*
    CAR_RENTAL_COMPANY_CAR 테이블에서 자동차 종류가 'SUV'인 자동차들의 평균 일일 대여 요금을 출력하는 SQL문 
    - 평균 일일 대여 요금은 소수 첫 번째 자리에서 반올림하고, 컬럼명은 AVERAGE_FEE 로 지정해주세요
*/

/* KEY POINT 
    1. AVG: 특정 column의 평균값을 계산하는 Aggregate Function
        - NULL 값을 자동으로 제외하고 평균값을 계산 
    2. ROUND(number, decimal): 반올림할 숫자, 자릿수로서 소수점 몇 번째 자리까지 남길지 결정
*/

select round(avg(daily_fee), 0) as average_fee
from car_rental_company_Car
where car_type = 'SUV'