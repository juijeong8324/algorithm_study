
from collections import deque


def solution(begin, target, words):
    if target not in words:  # 없으면 바로 0
        return 0

    q = deque()
    N = len(words)
    vis = {begin}
    words = set(words)  # 조회 시 O(1)

    q.append((begin, 0))
    path = 0
    while q:
        path += 1  # path 미리 업데이트
        for _ in range(len(q)):
            cur, path = q.popleft()

            for i in range(len(cur)):  # 현재 단어의 각 위치에 대해서
                for c in 'abcdefghijklmnopqrstuvwxyz':  # 바꿈
                    next = cur[:i] + c + cur[i+1:]

                    if next in words and next not in vis:
                        if next == target:
                            return path + 1
                        vis.add(next)
                        q.append((next, path+1))

    return 0  # 경로가 없는 경우
