# Input
# str1, str2 = 2~1000, 영문자만 유효 나머지는 글자 쌍 버리기
# 자카드 유사도
# A와 B의 교집합 / A와 B의 합집합
# 모두 공집합이면 1
# 중복 허용도 가능한 다중 집합으로 확장
# Output
# 두 문자열의 자카드 유사도
# 실수이므로 65536을 곱한 후에 소수점 아래를 버리고 정수부만 출력
# Hint
# dict, set
import re


def solution(str1, str2):
    A = {}  # 중복도 있을 수 있으니
    B = {}
    a = set()
    b = set()
    n, m = len(str1), len(str2)
    p = re.compile(r'[A-Za-z][A-Za-z]')
    for idx in range(n-1):
        temp = str1[idx:idx+2].lower()
        if p.findall(temp):
            a.add(temp)
            if temp in A:
                A[temp] += 1
            else:
                A[temp] = 1
    for idx in range(m-1):
        temp = str2[idx:idx+2].lower()
        if p.findall(temp):
            b.add(temp)
            if temp in B:
                B[temp] += 1
            else:
                B[temp] = 1

    intersection = a & b
    union = a | b
    ans1, ans2 = 0, 0  # 교집합, 합집합
    for i in intersection:
        ans1 += min(A[i], B[i])
    for j in union:
        ans2 += max(A.get(j, 0), B.get(j, 0))

    answer = 0.0
    if ans2 == 0:
        return 65536
    else:
        answer = ans1 / ans2 * 65536
    return int(answer)
