# Input
# n = 컴퓨터 개수 (1 이상 200 이하)
# computers = 연결에 대한 정보가 담긴 2차원 배열 (0부터 n-1인 정수)
# # i번 - j번 컴퓨터 연결: computers[i][j] = 1, 즉 양방향임을 알 수 있음
# Output
# 네트워크의 개수
# # 네트워크란
# # A - B → B - C → C - A임! = A,B,C는 모두 같은 네트워크!
# Hint
# DFS / BFS = 깊이든 너비든 연결된 노드를 모두 탐색
# 한번 방문했으면 탐색 취소

def solution(n, computers):
    network = 0
    visit = [0]*200

    for s in range(n):  # 모든 노드를 시작점
        if visit[s] == 1:
            continue

        stack = [s]  # 노드 번호
        visit[s] = 1  # 방문!
        network += 1

        # DFS
        while stack:
            node = stack.pop()

            for idx in range(n):
                if node == idx:  # 같은 노드면
                    continue
                if computers[node][idx] == 0:  # 연결되지 않았다면
                    continue
                if visit[idx] == 1:  # 이미 방문한 노드면
                    continue

                stack.append(idx)
                visit[idx] = 1

    return network
