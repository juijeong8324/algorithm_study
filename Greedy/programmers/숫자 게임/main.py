# Input
# A = A 팀원들이 부여받은 수가 출전 순서대로 나열되어 있는 배열 (N = 1~100,000)
# B = B[i]는 B팀의 i번 팀원이 부여받은 수를 의미하는 배열 (N = 1~100,000)
# Output
# A팀이 출전 순서를 공개했을 때 B팀이 얻을 수 있는 최대 승점 
# 규칙
# 무작위로 숫자를 부여 받고 A와 B가 나와 숫자 대결 (같으면 0점)
# Hint
# 조합? = N이 너무 커서 안 됨. (Time Complexity = N!)
# Greedy? = 현재 최소 값으로 그리디하게 승리! 못하면 pass

def solution(A, B):
    answer = 0
    N = len(A)
    
    # 정렬
    A = sorted(A)
    B = sorted(B)
    i = 0
    j = 0
    
    while i < N and j < N:
        if B[j] > A[i]: # B팀의 현재 최솟값으로 A팀의 현재 최솟값을 이길 수 있으면 승리
            answer += 1
            j += 1 # 
            i += 1
        else: # B팀의 현재 선수로는 이길 수 없으면, B팀의 다음 선수 시도
            j += 1
        
    return answer