# Input
# n = 지도의 한 변 크기
# " " = 공백 = 0, "#" = 벽 = 1
# arr1, arr2 = 2개의 정수 배열
# arr1, arr2 = or 연산
# Output
# '#', 공백으 해독된 문자열 배열
# Hint
# 2진수로 만든다
def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        map = arr1[i] | arr2[i]  # bit OR operate
        binary_string = format(map, f'0{n}b')  # int -> 2bit string, len 5
        ans = ""
        for ch in binary_string:
            ans += "#" if ch == "1" else " "
        answer.append(ans)

    return answer
