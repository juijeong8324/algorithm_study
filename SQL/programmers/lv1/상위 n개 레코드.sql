/*
    동물 보호소에 가장 먼저 들어온 동물의 이름을 조회하는 SQL 문을 작성
*/

/* KEY POINT
    1. LIMIT num: 전체 행에서 num만큼 RETURN
*/

-- 가장 효율적인 방식임
SELECT NAME
FROM ANIMAL_INS
ORDER BY DATETIME ASC
LIMIT 1

-- 집계함수 이용
SELECT NAME
FROM ANIMAL_INS
WHERE DATETIME = (SELECT MIN(DATETIME) FROM ANIMAL_INS) -- 서브쿼리로 table을 2번 scan해서 비효율적