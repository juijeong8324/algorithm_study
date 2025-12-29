/*
    FISH_INFO 테이블에서 잡은 물고기 중 가장 큰 물고기의 길이를 'cm' 를 붙여 출력하는 SQL 문을 작성
    - 컬럼명은 'MAX_LENGTH' 로 지정해
*/

/* KEY POINT 
    1. CONCAT(col1|str1, col2|str2, col3|str3, ...) : 여러 문자열 혹은 여러 column 값을 하나로 합쳐주는 함수
*/
select concat(max(length), 'cm') as max_length
from fish_info
