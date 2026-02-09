# Input
# n = 집합의 원소의 개수 (1~10000)
# s = 모든 원소들의 합 (1~100000000)
# Output
# 최고의 집합 (오름차순으로 정렬된 1차원 list로 return, 존재하지 않으면 -1 채우기)
# # 자연수 n개로 이루어진 multi set 중 다음 두 조건을 만족하는 집합 
# # 1. 각 원소의 합이 S가 되는 수 2. 1을 만족하면서 각 원소의 곱이 최대 
# Hint
# Greedy = 곱이 최대가 되려면 집합의 원소 간의 간격이 최소가 되어야 함

def solution(n, s):    
    # 예외 
    if s < n:
        return [-1]
    
    # 평균값
    num = s // n
    remainder = s % n # num보다 작은 값만큼 부족 (n개중 remainder개에 각각 +1로 분배)
    
    # num+1은 remainder개
    # num는 n-remainder개 만큼
    answer = [num] * (n - remainder) + [num + 1] * remainder
    
    return answer