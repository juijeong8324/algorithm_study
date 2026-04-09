# Input
# s = 0과 1로 이루어진 문자열 
# Output
# 이진 변환 1. x의 모든 0을 제거 2. x의 길이 c일 때, x를 x를 2빈법으로 표현한 문자열
# s가 "1"이 될 때까지 이진 변환할 때 그 횟수와 제거된 0의 개수 
# Hint
# format(n, 'b') or f"{n:b}"
# 문자열의 서식 지정을 위해 사용함! 보통 숫자를 예쁘게 출력하기 위해 사용 

def solution(s):
    answer = [0, 0] 
    
    while s != "1":
        size = len(s)
        count = 0
        for z in s: # count = s.count('0')
            if z == "0": count += 1
            
        s = format(size-count, 'b')
        answer[0] += 1
        answer[1] += count
    
    return answer