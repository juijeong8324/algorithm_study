/*
    USER_INFO 테이블에서 나이 정보가 없는 회원이 몇 명인지 출력하는 SQL문
    - 컬럼명은 USERS로 지정
*/

/* KEY POINT
    1. COUNT(*): NULL 포함 모든 행 
    2. COUNT(COL): 해당 COL의 값이 NULL이 아닌 모든 행 
*/

select count(*) as users
from user_info
where age is null

-- 이것도 된다ㅋㅋ
select count(*)-count(age) as users
from user_info