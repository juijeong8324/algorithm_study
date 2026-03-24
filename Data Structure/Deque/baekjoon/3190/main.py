import sys
from collections import defaultdict, deque
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

dx = [0, 1, 0, -1] 
dy = [1, 0, -1, 0] # 오, 아, 왼, 위

def main():
    # input
    N = int(input().strip())
    K = int(input().strip())
    board = [[0]* (N+1) for _ in range(N+1)]
    turn = defaultdict(int)

    for i in range(K):
        A,B = map(int, input().strip().split())
        board[A][B] = 1

    L = int(input().strip())

    for i in range(L):
        X, C = input().strip().split()
        X = int(X)
        turn[X] = C

    snake = deque([(1, 1)]) # 뱀의 좌표 
    d = 0 # 뱀의 머리 방향
    time = 0 
    # Game Start
    while True:
        time += 1 
        # 이동  
        x, y = snake[0] # 현재 머리
        x = x + dx[d]
        y = y + dy[d]

        if x <= 0 or x > N or y <= 0 or y > N: # 벽 
            break
        if board[x][y] == 1: # 사과
            board[x][y] = 0 
        elif (x, y) in snake: # 뱀 몸통
            break
        else: 
            snake.pop() # 꼬리 제거

        snake.appendleft((x, y)) # 새로운 머리 추가 
        
        if time in turn: # 방향 전환
            if turn[time] == 'L': 
                d -= 1
                d = d % 4
            else: 
                d += 1
                d = d % 4

    print(time)

main()