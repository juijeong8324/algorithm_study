# Input
# n = 화살의 개수 (1~10)
# info = 어피치의 과녁 점수 개수 10점 부터 0점까지 (길이 = 11)
# Output
# 가장 큰 점수 차이로 우승하기 위해 어떤 과녁에 맞춰야 하는가?
# 라이언이 지거나 비기는 경우 -1
# 여러 개인 경우 가장 낮은 점수를 더 많이 맞힌 경우를 return
# Rule
# 과녁의 점수 k는 a발 < b발인 경우에 대해서 라이언이 가져간다.
# a발 >= b발인 경우 어피치가 가져간다.
# Hint
# 라이언이 점수를 얻으려면 어피치의 화살 개수보다 1개 더 많으면 된다. == n+1이거나 0이면 된다.
# Greedy = 점수를 얻기 위해 최소한의 화살 개수를 사용한다.
# Brute Force = 점수를 얻거나 얻지 않거나 2가지의 경우의 수가 존재 2^10 시간 복잡도 충분함!


from itertools import product


def solution(n, info):
    answer = []
    # 라이언이 과녁을 맞칠 수 있는 모든 경우의 수
    lions = list(product([0, 1], repeat=10))
    max_diff = 0  # 최대일 때

    for lion in lions:
        temp_score = 0
        ap_score = 0
        result = [l*i + 1 if l else 0 for l,
                  i in zip(lion, info)]  # 라이언의 화살 개수
        if sum(result) > n:  # 화살 개수가 n보다 큰 경우
            continue
        result += [n - sum(result)]  # 0점 화살 개수

        for idx, p in enumerate(zip(result, info)):  # 총점 계산
            if p[0] > p[1]:
                temp_score += 10-idx
            elif p[0] < p[1]:
                ap_score += 10-idx

        if ap_score < temp_score:  # 어피치보다 크고
            temp = temp_score-ap_score
            if max_diff < temp:  # 차이가 클 때
                answer = result
                max_diff = temp
            elif max_diff == temp:
                for i in range(11, -1, -1):  # 뒤에서 부터
                    if sum(result[i:]) > sum(answer[i:]):
                        answer = result
                        break  # 바로 종료
    if not answer:
        return [-1]

    return answer
