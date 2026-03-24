from collections import deque


def solution():
    N, M = map(int, input().split())
    board = []
    dx = [1, 0, -1, 0] # 아, 오, 위, 왼
    dy = [0, 1, 0, -1]
    red = ()
    blue = ()
    time = 0

    for i in range(N):
        row = input().strip()
        r = []
        for j in range(len(row)):
            r.append(row[j])
            if 'R' == row[j]:
                red = (i, j)
                r[j] = '.'
            elif 'B' == row[j]:
                blue = (i, j)
                r[j] = '.'
        
        board.append(r)


    def move(tx, ty, dx, dy, ox, oy): # 현재 좌표, 방향, 상대 좌표
        while 0 <= tx < N and 0 <= ty < M and board[tx][ty] != '#': 
            if board[tx][ty] == 'O':
                return tx, ty, True 
            if tx == ox and ty == oy:  # 상대 구슬에 막힌 상황 
                break
            tx += dx
            ty += dy

        tx -= dx
        ty -= dy

        return tx, ty, False

    q = deque()
    visited = set()
    q.append((red[0], red[1], blue[0], blue[1], 0)) # red, blue, time
    visited.add((red[0], red[1], blue[0], blue[1])) # R과 B의 move 체크, 이때 R, B 각각의 방문을 기록하는 것이 아님

    while q:
        rx, ry, bx, by, time = q.popleft()
        if time >= 10: continue

        for x, y in zip(dx, dy):
            nrx, nry, nbx, nby = rx, ry, bx, by # 초기화 
            if x == 1: first_r = rx >= bx # 아래
            elif x == -1: first_r = rx <= bx# 위
            elif y == 1: first_r = ry >= by# 오른쪽
            else: first_r = ry <= by# 왼쪽

            if first_r:
                nrx, nry, r_hole = move(nrx, nry, x, y, nbx, nby)
                nbx, nby, b_hole = move(nbx, nby, x, y, nrx, nry)
            else:
                nbx, nby, b_hole = move(nbx, nby, x, y, nrx, nry)
                nrx, nry, r_hole = move(nrx, nry, x, y, nbx, nby)

            if b_hole: continue
            if r_hole:
                print(time+1)
                return 
            if (nrx, nry, nbx, nby) not in visited: # R과 B의 move가 이미 방문 했더라면 
                visited.add((nrx, nry, nbx, nby))
                q.append((nrx, nry, nbx, nby, time+1))

    print(-1)
        
solution()