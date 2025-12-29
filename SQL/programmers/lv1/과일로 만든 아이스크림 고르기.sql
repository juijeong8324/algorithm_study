/*
    상반기 아이스크림 총주문량이 3,000보다 높으면서 아이스크림의 주 성분이 과일인 아이스크림의 맛을 총주문량이 큰 순서대로 조회하는 SQL문
    - 상반기 주문 정보 : first_half 테이블 
    - 아이스크림 성분에 대한 정보 : icecream_info 테이블
*/

/* KEY POINT 
    1. JOIN: 두 개 이상의 table에서 공통 key(column)를 기준으로 연결해서 조회하는 방법
        - SELECT A.col1 B.col2
          FROM A
          INNER JOIN B ON A.C = B.C
          : A와 B 테이블에서 A.C = B.C인 일치하는 행들에 대해서 A.col1, B.col2만을 반환
        - FROM -> JOIN -> WHERE 순서로 실행 (이떄 WHERE은 합쳐진 임시 table에 대해서 조건 수행)
*/

select f.flavor
from first_half f
inner join icecream_info i on f.flavor = i.flavor
where f.total_order >= 3000 and i.ingredient_type = 'fruit_based'
order by f.total_order desc


-- 서브 쿼리 이용하는 방법 == 비효율적임.
-- first_half의 행 개수가 N, icecream_info의 행 개수가 M일 떄, O(NM) Time Complexity가 걸림
SELECT FLAVOR
FROM FIRST_HALF
WHERE TOTAL_ORDER > 3000 AND FLAVOR IN (
    SELECT FLAVOR
    FROM ICECREAM_INFO
    WHERE INGREDIENT_TYPE = 'fruit_based')
ORDER BY TOTAL_ORDER DESC;