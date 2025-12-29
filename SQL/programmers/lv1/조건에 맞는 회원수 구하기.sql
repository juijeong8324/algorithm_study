/* 
USER_INFO 테이블에서 2021년에 가입한 회원 중 나이가 20세 이상 29세 이하인 회원이 몇 명인지 출력하는 SQL문
*/

/* KEY POINT
    1. JOINED는 DATE 형식: YEAR(), MONTH(), DAY, WEEK
    2. = (값이 같다, 비교연산자임), != (값이 같지 않다), NULL일 때는 IS 연산자로!
    3. BETWEEN 키워드를 사용하자
*/

SELECT COUNT(USER_ID) AS USERS
FROM USER_INFO
WHERE YEAR(JOINED) = 2021 AND (AGE BETWEEN 20 AND 29)