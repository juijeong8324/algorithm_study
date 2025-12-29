/*
동물 보호소에 들어온 동물 중, 이름이 없는 채로 들어온 동물의 ID를 조회하는 SQL
- 단, ID는 오름차순 정렬
*/

-- KEY POINT
-- 실행순서 FROM -> WHERE -> GROUP BY -> HAVING BY -> SELECT -> ORDER BY

SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NULL
ORDER BY ANIMAL_ID;
