# Input
# n = 자연수 (10,000 이하)
# Output
# 연속된 자연수들로 n을 표현하는 방법의 수 
# Hint
# Brute Force -> 시작점을 기준으로 매번 처음부터 계산 -> 시간복잡도 O(N^2)
# Two Pointer -> start/end 두 포인터를 두고 합이 작으면 end++, 크면 start++ -> O(N)

def solution(n):
    start = 1 # 시작점 
    end = start # 끝점
    temp_sum = start
    answer = 1 # n 자기자신 포함 
    
    # 예외 조건 
    if n == 1:
        return answer
    
    while start != n and end != n: # 둘 중 하나라도 n에 도달하면 더 이상 연속된 구간 없음
        if temp_sum < n: # 작다면 end를 늘리기 
            end += 1
            temp_sum += end
        elif temp_sum > n: # 크다면 start를 늘리기 
            temp_sum -= start
            start += 1
        else: # 같은 경우 start를 늘리기 
            answer += 1
            temp_sum -= start
            start += 1
    
    return answer

