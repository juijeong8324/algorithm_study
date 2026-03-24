# 구슬 탈출 2

## 문제

- **Input**

  # Input
  - `N`, `M` = 보드의 행과 열 (3~10)
  - . / # / O / R / B (빈 칸, 장애물, 구멍 위치, 빨간 구슬, 파란 구슬)
  - 구멍 개수는 1개, 빨간 구슬 1개, 파란 구슬 1개

- **Output**
  - 기울이기를 통해 구슬을 이동시킬 때, 최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는가?
    - 기울이는 동작을 그만하는 것은 더 이상 구슬이 움직이지 않을 때 까지
  - 왼 오 위 아 로 네 가지 동작 가능
  - 실패 시 `-1` 출력
    - 파란 구슬이 빠지면
    - 10번 이하로 빼낼 수 없으면

<br>
<br>

## Key point

- **BFS**
  - 최소 이동 거리로 구슬의 위치를 찾아야 한다.
  - **`state = (rx,ry,bx,by)`**
    - 이때 두 구슬이 동시에 움직이므로 구슬 쌍이 움직인 좌표를 체크해야 한다.

- **Simulation**
  - 한 move에 여러 칸을 이동할 수 있어야 한다.
    - 한 번의 기울이기로 여러 칸 이동 가능 → 기울인 후 최종 좌표를 state로 사용
  - **이동 순위 우선 체크**
    - 두 구슬이 같은 방향으로 이동한다면 충돌 방지를 위해 이동방향에 따라 우선순위를 정해서 구슬을 이동시켜야 함

<br>
<br>

## Algorithm Approach

1. state 정보

```python
    q.append((red[0], red[1], blue[0], blue[1], 0))
```

BFS 큐에 빨간 구슬 좌표, 파란 구슬 좌표, 이동 횟수를 함께 저장. 이동 횟수는 종료 조건을 위함

<br>

2. 4방향 탐색 — 이동 우선순위 결정 후 move

```python
    for x, y in zip(dx, dy):
        nrx, nry, nbx, nby = rx, ry, bx, by # 초기화
        if x == 1: first_r = rx >= bx # 아래
        elif x == -1: first_r = rx <= bx# 위
        elif y == 1: first_r = ry >= by# 오른쪽
        else: first_r = ry <= by# 왼쪽

        if first_r: # 빨간 구슬 먼저
            nrx, nry, r_hole = move(nrx, nry, x, y, nbx, nby)
            nbx, nby, b_hole = move(nbx, nby, x, y, nrx, nry)
        else:
            nbx, nby, b_hole = move(nbx, nby, x, y, nrx, nry)
            nrx, nry, r_hole = move(nrx, nry, x, y, nbx, nby)
```

두 구슬이 같은 방향으로 이동할 때 충돌을 막기 위해, 이동 방향 기준으로 더 앞에 있는 구슬을 먼저 이동.

<br>

1. move 함수

```python
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
```

벽(`#`) 또는 범위를 벗어날 때까지 이동하며, 세 가지 종료 조건을 처리한다:

- 구멍(`O`)을 만나면 → 현재 위치 반환 + `True` (구멍에 빠짐)
- 상대 구슬 위치와 겹치면 → 한 칸 되돌아가고 종료 (충돌)
- 벽/범위 끝에 닿으면 → 한 칸 되돌아가고 종료
