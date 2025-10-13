# Input
# numbers = 이진트리로 만들고 싶은 수를 담은 1차원 정수 배열
# Output
# numbers에 주어진 순서대로 하나의 이진트리로 해당 수를 표현할 수 있는지 1차원 boolean 배열
# 1. 이진수 저장할 빈 문자열 생성
# 2. 주어진 이진트리에 더미 추가 -> 포화 이진 트리 생성! -> 루프 노드는 그대로 유지
# 3. 포화 이진 노드들의 가장 왼쪽부터 오른쪽까지 살펴봄! -> 높이와 상관없음
#    = 리프가 아닌 노드 -> 왼쪽 서브 트리보다 오른쪽, 오른쪽 서브 트리보다 왼쪽에 있다 가정
# 4. 살펴본 노드가 더미면 문자열 뒤에 0 추가, 아니라면 문자열 뒤에 1 추가
# 5. 이진수 -> 십진수
# Hint
# 포화 상태 전체 노드 개수 = 이진수의 전체 길이
# Divice and Conquer = sub tree로 분할 한 후 각각 노드가 유효한지 확인
# Biary Search = root를 찾기 위함


def isValidTree(s):
    if len(s) == 0:  # 리프노드 인 경우
        return 1

    mid = (0 + len(s) - 1) // 2
    left_sub = s[:mid]
    right_sub = s[mid+1:]

    if s[mid] == "0":  # root가 0인 경우
        if "1" in left_sub or "1" in right_sub:
            return 0
        else:
            return 1
    else:  # root가 1인 경우
        return isValidTree(left_sub) and isValidTree(right_sub)


def solution(numbers):
    answer = []

    for n in numbers:
        s = bin(n)[2:]

        # 포화 이진 트리로 만들기
        h = 1
        n = len(s)

        while (2**h)-1 < n:  # 이진 트리 전체 노드 개수 < s 길이
            h += 1
        target = (2**h)-1
        s = "0" * (target-n) + s

        ans = isValidTree(s)
        answer.append(ans)

    return answer
