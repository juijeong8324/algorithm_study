from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(board, target):  # Find all Puzzles shape with target
    puzzles = []
    N = len(board)
    vis = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if vis[i][j] == 0 and board[i][j] == target:
                q = deque([(i, j)])
                vis[i][j] = 1
                p = [(i, j)]  # a current puzzle piece

                while q:
                    curX, curY = q.popleft()

                    for k in range(4):
                        x, y = curX + dx[k], curY + dy[k]

                        if x < 0 or x >= N or y < 0 or y >= N:
                            continue  # out of bounds
                        if vis[x][y] == 1 or board[x][y] != target:
                            continue  # already visited or not target

                        p.append((x, y))
                        q.append((x, y))
                        vis[x][y] = 1

                puzzles.append(p)  # Add a puzzle piece

    return puzzles


def translate(puzzle):  # Translate to (0,0)
    minX, minY = 1e9, 1e9
    for x, y in puzzle:
        minX = min(minX, x)
        minY = min(minY, y)

    return [(x-minX, y-minY) for x, y in puzzle]


def rotate(puzzle):  # Rotate 90 degrees and translate
    rotate_puzzle = [(y, -x) for x, y in puzzle]
    return translate(rotate_puzzle)

# Main


def solution(game_board, table):
    answer = 0
    p1 = bfs(game_board, 0)
    p2 = bfs(table, 1)
    used = [0]*len(p2)

    # Match game board with table puzzles
    for game_p in p1:
        flag = False  # If match, then search next game_p
        for idx, table_p in enumerate(p2):
            if not used[idx] and len(game_p) == len(table_p):  # Unused and same size
                temp_game = translate(game_p)
                temp_table = translate(table_p)
                for i in range(4):  # Check all 4 rotations
                    # Compare contents (==), not references (is)
                    if sorted(temp_game) == sorted(temp_table):
                        answer += len(temp_game)
                        used[idx] = 1
                        flag = True
                        break
                    # If not
                    temp_table = rotate(temp_table)

            if flag:
                break

    return answer
