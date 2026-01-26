# Input
# begin, target, words(3개 ~ 50개, 중복되는 단어는 없다!!!!!!!!!!)
# 모든 단어의 길이는 같다. begin과 target은 같지 않다.
# Output
# 규칙에 따라 begin에서 target으로 변환하는 가장 짧은 변환 과정 횟수
# 1. 한 번에 한 개의 알파벳만 바꿀 수 있다.
# 2. words에 있는 단어로만 변환할 수 있다.
# words에 없는 target이면 0 return

from collections import deque


def check(target, words):  # 1씩 차이나는 단어 찾기
    diff_count = 0
    for a, b in zip(target, words):
        if a != b:
            diff_count += 1
        if diff_count > 1:
            return False

    return diff_count == 1


def solution(begin, target, words):
    if target not in words:  # 없으면 바로 0
        return 0

    q = deque()
    N = len(words)
    vis = set()

    q.append((begin, 0))
    while q:
        cur, path = q.popleft()

        for w in words:
            if w in vis:
                continue  # 이미 방문했다면
            if check(cur, w):  # diff가 1인 경우에 대해서
                # 답인 경우
                if w == target:
                    return path + 1

                vis.add(w)
                q.append((w, path+1))

    return 0  # 경로가 없는 경우

# path를 저장 안 하는 경우
# 즉 BFS의 같은 level은 같은 거리를 갖는다를 이용


def solution(begin, target, words):
    if target not in words:  # 없으면 바로 0
        return 0

    q = deque()
    N = len(words)
    vis = {begin}

    q.append(begin)
    path = 0
    while q:
        path += 1  # path 미리 업데이트
        for _ in range(len(q)):
            cur = q.popleft()
            for w in words:  # 현재 level의 node(즉 거리가 모두 path로 같은 노드)를 탐색
                if w in vis:
                    continue
                if check(cur, w):  # diff가 1인 경우에 대해서
                    # 답인 경우
                    if w == target:
                        return path

                    vis.add(w)
                    q.append(w)

    return 0  # 경로가 없는 경우
