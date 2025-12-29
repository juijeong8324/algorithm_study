/*
    PATIENT 테이블에서 12세 이하인 여자환자의 환자이름, 환자번호, 성별코드, 나이, 전화번호를 조회하는 SQL문을 작성
    - 전화번호가 없는 경우, 'NONE'으로 출력
    - 결과는 나이를 기준으로 내림차순 정렬
    - 나이 같다면 환자이름을 기준으로 오름차순 정렬
*/

-- coalesce 
select pt_name, pt_no, gend_cd, age, coalesce(tlno, 'NONE') as tlno
from patient
where gend_cd = 'W' and age <= 12
order by age desc, pt_name asc

-- case 
select pt_name, pt_no, gend_cd, age, 
        case when tlno is null then 'NONE' else tlno end as tlno
from patient
where gend_cd = 'W' and age <= 12
order by age desc, pt_name asc