/*
DOCTOR 테이블에서 진료과가 흉부외과(CS)이거나 일반외과(GS)인 의사의 이름, 의사ID, 진료과, 고용일자를 조회
- 고용일자를 기준으로 내림차순 정렬하고, 고용일자가 같다면 이름을 기준으로 오름차순 정렬
*/

/* KEY POINT
    1. DATE_FORMAT(COLUMN, 형식)
        %Y - 4자리 연도 (2021), %y - 2자리 연도 (21), %m - 월 (01~12), %d - 일 (01~31) 
    2. COLUMN IN (A, B, ..): 특정 COL의 값이 여러 값 중 하나와 일치하는지 확인, OR 연산 여러 개와 같은 효과
    3. ORDER BY COL1 (ASC|DESC), COL2(ASC|DESC) ... : COL1에서 정렬 -> COL1의 값이 일치하는 행들은 다시 COL2에서 정렬
*/

SELECT DR_NAME, DR_ID, MCDP_CD, DATE_FORMAT(HIRE_YMD, '%Y-%m-%d') AS HIRE_YMD
FROM DOCTOR
WHERE MCDP_CD IN ('CS', 'GS')
ORDER BY HIRE_YMD DESC, DR_NAME ASC 