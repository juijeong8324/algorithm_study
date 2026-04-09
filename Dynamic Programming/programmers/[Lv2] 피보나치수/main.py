# Input
# n = 2이상 100,000 이하인 자연수 
# Output
# n번째 피보자치 수를 1234567로 나눈 나머지를 리턴 
# Hint
# 재귀면 같은 연산을 반복해서 -> O(N^2)
# DP = 이전의 정보를 저장해서 재사용 -> O(N)으로 해결 

def solution(n):
    fibo = [0]*(n+1)
    
    # 초기값 계산 
    fibo[1] = 1
    
    # DP
    for i in range(2, n+1):
        fibo[i] = fibo[i-2] + fibo[i-1] # Python은 정수 크기 제한 없음, 메모리를 동적으로 늘려서 저장하므로..! 
    
    return fibo[n] % 1234567