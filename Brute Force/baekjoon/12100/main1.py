import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def main():
    N = int(input().strip())
    dx = [1, -1, 0, 0] # 하, 상, 오, 왼
    dy = [0, 0, 1, -1]
    board = []

    for _ in range(N):
        row = list(map(int, input().strip().split()))
        board.append(row)

    def transpose(temp_board): # column -> row 
        new_board = [[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                new_board[j][i] = temp_board[i][j]

        return new_board

    def move(temp_board): # move left
        new_board = []
        for row in temp_board:
            row = [x for x in row if x != 0]
            merged_row = []
            idx = 0
        
            while idx < len(row):
                if idx+1 < len(row) and row[idx] == row[idx+1]:
                    merged_row.append(row[idx]*2)
                    idx += 2
                else:
                    merged_row.append(row[idx])
                    idx += 1

            merged_row += [0] * (N - len(merged_row))
            new_board.append(merged_row)

        return new_board

    def dfs(cnt, board):
        if cnt == 5:
            return max(board[i][j] for i in range(N) for j in range(N))

        result = 0
        prev = [row[:] for row in board]
        for x, y in zip(dx, dy):
            if x == -1: # 위로 
                temp = transpose(prev)
                temp_board = move(temp)
                temp_board = transpose(temp_board)
            elif x == 1: # 아래로 
                temp = transpose(prev)
                temp = [row[::-1] for row in temp]
                temp_board = move(temp)
                temp_board = [row[::-1] for row in temp_board]
                temp_board = transpose(temp_board)
            elif y == 1: # 오른쪽 
                temp = [row[::-1] for row in prev]
                temp_board = move(temp)
                temp_board = [row[::-1] for row in temp_board]
            else: # 왼쪽 
                temp_board = move(temp)

            result = max(result, brute_force(cnt+1, temp_board))

        return result

    answer = dfs(0, board)
    print(answer)
    
main()