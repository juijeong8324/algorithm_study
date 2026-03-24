import sys
input = sys.stdin.readline

def move_left(board, N):
    new_board = []
    for row in board:
        tiles = [x for x in row if x != 0]
        merged = []
        skip = False
        for i in range(len(tiles)):
            if skip:
                skip = False
                continue
            if i + 1 < len(tiles) and tiles[i] == tiles[i+1]:
                merged.append(tiles[i] * 2)
                skip = True
            else:
                merged.append(tiles[i])
        merged += [0] * (N - len(merged))
        new_board.append(merged)
    return new_board

def rotate(board, N):
    new_board = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_board[j][N-1-i] = board[i][j]
    return new_board

def move(board, N, direction):
    for _ in range(direction): # rotate
        board = rotate_90(board, N)
    board = move_left(board, N) # 이동
    for _ in range(4 - direction): # 복구
        board = rotate_90(board, N)
    return board

def dfs(board, N, cnt):
    if cnt == 5:
        return max(board[i][j] for i in range(N) for j in range(N))
    
    result = 0
    for d in range(4):
        new_board = move([row[:] for row in board], N, d) # 각 방향마다 이동한 board 결과
        result = max(result, dfs(new_board, N, cnt + 1))
    
    return result

def main():
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    print(dfs(board, N, 0))

main()