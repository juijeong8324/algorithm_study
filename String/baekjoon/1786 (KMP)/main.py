import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def solution():
    T = input().rstrip('\n') # strip()은 양쪽 공백까디 제거함....
    P = input().rstrip('\n')
    N = len(T)
    M = len(P)

    # Fail Function
    # P[:i]까지 matching된 index
    fail = [0]*M  
    j = 0
    
    for i in range(1, M):
        while j > 0 and P[i] != P[j]: # 
            j = fail[j-1] # 새로 비교해봐야 할 P의 prefix 
        
        if P[i] == P[j]:
            j += 1
            fail[i] = j

    # Macthing 
    idx_P = 0 # index for P 
    count = 0
    answer = []
    for idx_T in range(N): # start index for T 
        while idx_P > 0 and T[idx_T] != P[idx_P]: # 같지 않다면 
            idx_P = fail[idx_P-1]
        
        # 같다면 
        if T[idx_T] == P[idx_P]:
            idx_P += 1

        if idx_P == M:
            count += 1
            answer.append(idx_T-M+2) # 1-index 
            idx_P = fail[idx_P-1]

    print(count)
    print(*answer)
    

solution()