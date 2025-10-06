# Input
# m, n, board = 판의 높이(행), 폭(열), 배치 정보
# Output
# 지울 블록 개수
# 2 x 2로 배치된 블록을 삭제
# 빡구현...

def solution(m, n, board):
    answer = 0
    temp = -1
    col_board = []
    for col in range(n):
        col_str = "".join(board[row][col] for row in range(m - 1, -1, -1))
        col_board.append(col_str)

    while temp != 0:
        map = [[0 for _ in range(m)] for _ in range(n)]  # 초기화
        # 박스 찾기
        for col in range(n):
            for row in range(m):
                if col + 1 >= n or row + 1 >= m:
                    continue
                if col_board[col][row] == "#":
                    continue
                flag = (col_board[col][row] == col_board[col+1][row]) and (col_board[col][row]
                                                                           == col_board[col][row+1]) and (col_board[col][row] == col_board[col+1][row+1])
                if flag:
                    map[col][row] = 1
                    map[col+1][row] = 1
                    map[col][row+1] = 1
                    map[col+1][row+1] = 1

        temp = sum(sum(x) for x in map)
        answer += temp

        # delete
        for col in range(n):  # 현재 열
            new_col = ""
            for row in range(m):
                if not map[col][row]:
                    new_col += col_board[col][row]
            new_col = f"{new_col:#<{m}}"
            col_board[col] = new_col

    return answer
