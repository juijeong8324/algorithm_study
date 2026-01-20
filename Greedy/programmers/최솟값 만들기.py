# Input
# A, B = 배열의 크기 (1000 이하 자연수), 원소의 크기 (1000 이하 자연수) / 각 배열은 자연수로 이루어짐. 
# Output
# 최종적으로 누적된 최솟값 
# A, B에서 각각 한 개의 숫자를 뽑아 두 수를 곱함 
# 배열의 길이만큼 반복 
# 두 수를 곱한 값을 누적하여 더함
# 한 번 뽑으면 다시 뽑을 수 없음 
# Hint 
# 누적값이 최소가 되려면 매번 (A , B)에서 (최대, 최소) 조합이 되어야 함.

def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    
    for a, b in zip(A,B):
        answer += a*b
    
    return answer