# 참가자 이름의 hash 값을 key로 한 dict를 생성
# hash값을 누적합하여 활용

def solution(participant, completion):
    answer = ''
    total_hash = 0
    dic = {}

    for part in participant:
        dic[hash(part)] = part  # dict의 key = hash(참가자)
        total_hash += int(hash(part))  # hash 값을 더함 (중복이 있을 수 있으므로)
    for com in completion:
        total_hash -= hash(com)  # 특정 key에 해당하는 hash 값을 제거
    answer = dic[total_hash]  # 남은 숫자값에 해당하는 이름 반환

    return answer
