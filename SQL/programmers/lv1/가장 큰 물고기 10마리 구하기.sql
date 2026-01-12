/*
    FISH_INFO 테이블에서 가장 큰 물고기 10마리의 ID와 길이를 출력하는 SQL 문
    - 결과는 길이를 기준으로 내림차순 정렬
    - 길이가 같다면 물고기의 ID에 대해 오름차순 정렬
    - 단, 가장 큰 물고기 10마리 중 길이가 10cm 이하인 경우는 없다. 
    - ID 컬럼명은 ID, 길이 컬럼명은 LENGTH!
*/

/* KEY POINT 
    1. LIMIT num: 전체 행에서 num만큼 RETURN
*/

select id, length
from fish_info
order by length desc, id asc
limit 10