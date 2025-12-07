# Input
# arr = 연속적으로 나타나는 숫자가 포함된 배열
# elemet_size = 0 ~ 9
# size = 1,000,000 이하의 자연수
# Output
# 연속적으로 나타나는 숫자는 하나만 남기고 제거한 배열 arr
# 단, 순서는 유지해야 함!
# Hint
# 연속적이지 않은 숫자 배열을 담을 저장소 == stack

# Method1: 원소값이 아닌 마지막 원소값을 포함한 리스트로 비교
def solution(arr):
    stack = []
    for n in arr:
        if stack[-1:] == [n]:
            continue
        stack.append(n)
    return stack

# Method2: 스택을 위한 list 생성 후 스택의 top과 arr의 원소 값이 같지 않을 때만 추가


def solution(arr):
    stack = []
    for n in arr:
        if len(stack) == 0 or stack[-1] != n:
            stack.append(n)
    return stack
