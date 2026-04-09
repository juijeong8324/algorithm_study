# Input
# brown = 카펫에서 본 갈색 격자의 수 (8이상 5,000 이하 자연수)
# yellow = 노란색 격자의 수 (1 이상 2,000,000 이하 자연수)
# 가로 >= 세로 
# Output
# 카펫의 가로, 세로 크기
# 테두리 1줄은 갈색이고 내부는 노란색
# Hint
# 수학임
# 핵심은 탐색 조사 범위를 어떻게 줄일 것인가..!

# 1. N*M = brown + yellow / 2. 2*N + 2*M - 4 = brown을 만족하는 이차방정식을 찾으면 됨
def solution(brown, yellow):
    total = brown + yellow
    s = (brown + 4) // 2 # N + M
    
    for M in range(3, s):
        N = s - M # 2번 만족
        if N * M == total: # 1번 만족
            return [max(N, M), min(N, M)]

# brown N x M yellow (N-2) x (M-2) 임을 이용 
def solution(brown, yellow):
    answer = []
    N = 0
    M = 3
    
    total = brown + yellow
    bound = total // 2
    while M <= bound:
        if total % M == 0:
            N = total // M
            if (N-2)*(M-2) == yellow:
                answer.append(N)
                answer.append(M)
                break
        M += 1

    
    return answer

