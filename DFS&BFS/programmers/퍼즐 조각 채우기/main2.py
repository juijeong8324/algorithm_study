# 한 퍼즐의 rotation들을 미리 계산하여 저장하는 방식.
# 이게 더 깔끔함!!!

from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(board, target):
    puzzles = []
    N = len(board)
    vis = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if vis[i][j] == 0 and board[i][j] == target:
                q = deque([(i, j)])
                vis[i][j] = 1
                shape = [(i, j)]

                while q:
                    cx, cy = q.popleft()

                    for k in range(4):
                        x, y = cx + dx[k], cy + dy[k]

                        if x < 0 or x >= N or y < 0 or y >= N:
                            continue
                        if vis[x][y] == 1 or board[x][y] != target:
                            continue

                        shape.append((x, y))
                        q.append((x, y))
                        vis[x][y] = 1

                puzzles.append(shape)

    return puzzles


def translate(shape):
    minX = min(x for x, y in shape)
    minY = min(y for x, y in shape)

    return sorted([(x-minX, y-minY) for x, y in shape])


def get_rotations(shape):  # 퍼즐의 모든 회전 반환
    rotations = []
    current = shape

    for _ in range(4):
        rotations.append(translate(current))
        current = [(y, -x) for x, y in current]

    return rotations

# Main


def solution(game_board, table):
    answer = 0
    board_shapes = bfs(game_board, 0)
    table_shapes = bfs(table, 1)

    # 각 table의 모든 회전 형태 미리 계산
    table_rotations = [get_rotations(shape) for shape in table_shapes]

    used = [False] * len(table_shapes)
    # 각 game_board의 빈칸마다 table 퍼즐 비교
    for board_shape in board_shapes:
        if len(used) == sum(used):  # 모든 table 퍼즐 사용한 경우
            break

        board = translate(board_shape)
        for idx, rotations in enumerate(table_rotations):
            if not used[idx]:  # 안 사용한 table 퍼즐에 대해서
                if board in rotations:
                    answer += len(board)
                    used[idx] = True
                    break

    return answer
