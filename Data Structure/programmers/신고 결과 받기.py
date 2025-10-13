# Input
# id_list = 이용자의 ID가 담긴 str 배열 (1~1000, 중복 X)
# report = 각 이용자가 신고한 이용자의 ID 정보가 담긴 문자열 배열 (1~200000)
# k = 정지 기준 신고 횟수
# Output
# 게시판 불량 이용자 신고하고 처리 결과 메일 발송 시스템
# 1. 각 유저는 한 번에 한 명의 유저 신고, 신고 횟수 제한 X, 한 유저 여러 번 신고해도 동일 유저에 대해 1회
# 2. k번 이상 신고한 유저는 정지, 해당 유저를 신고한 모든 유저에게 메일 발송
# 각 유저별 처리 결과 메일을 받은 횟수
# Hint
# search를 쉽게
# dict = 신고 당한 유저를 모은 자료구조
# set = 각 유저의 신고한 ID를 모은 자료 구조

def solution(id_list, report, k):
    answer = {x: 0 for x in id_list}  # 답
    count = {x: [] for x in id_list}  # 신고당한 ID : 신고한 ID

    for r in set(report):
        id_user, user = r.split()
        count[user].append(id_user)

    for key, value in count.items():
        if len(value) >= k:  # 정지될 유저인가?
            for id_user in value:  # 신고한 ID에 대해서
                answer[id_user] += 1

    answer = list(answer.values())
    return answer
