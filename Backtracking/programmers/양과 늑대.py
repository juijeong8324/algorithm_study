# Input
# info = 각 노드에 있는 양 또는 늑대에 대한 정보가 담긴 배열 (2~17), 0=양 1=늑대
# edges = 2진 트리의 각 노드르의 연결 관계, [부모 노드 번호, 자식 노드 번호]
# Output
# 다음과 같은 조건에 따라 각 노드를 방문하며 모을 수 있는 양 최대 마리 수
# 내가 모은 양의 수 <= 늑대의 수 -> 양의 수=0
# Hint
# 백트래킹임!! == 현재 노드에 대해서 모든 방문 가능한 노드들 (양 > 늑대)에 대해 방문!
# 단순 DFS는 아님!! == 즉 무조건 현재 노드에서 자식 노드로 갈 필요 없음
# 결국 방문 순서가 중요!

def solution(info, edges):
    answer = 0  # 양의 개수
    edge = {}  # dict
    # 그래프 만들기
    for e in edges:
        if e[0] in edge:
            edge[e[0]].append(e[1])
        else:
            edge[e[0]] = [e[1]]

    def dfs(node, sheep, wolf, search):
        nonlocal answer  # python scope 문제

        if not info[node]:  # 양이면
            sheep += 1
            answer = max(answer, sheep)
        else:  # 늑대면
            wolf += 1

        if sheep <= wolf:  # 종료 조건
            return

        next_visit = set(search)  # 복사
        if node in edge:  # leaf node가 아닌 경우에
            next_visit.update(edge[node])

        for next_n in next_visit:
            new_set = next_visit - {next_n}  # 방문할 노드를 제외한 나머지 방문 가능한 노드들
            dfs(next_n, sheep, wolf, new_set)

    dfs(0, 0, 0, set())

    return answer
