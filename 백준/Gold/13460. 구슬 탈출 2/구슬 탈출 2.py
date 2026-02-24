import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
grid = [input().rstrip() for _ in range(N)]
visited = []

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def get_pos():
    rr, rc, br, bc = 0,0,0,0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'B':
                br, bc = i, j
            if grid[i][j] == 'R':
                rr, rc = i, j
    return rr, rc, br, bc

def move(x, y, dx, dy):
    cnt = 0
    # 이동하는 위치가 벽 아니고 구멍에 들어가지 않을 동안 반복
    while grid[x + dx][y + dy] != "#" and grid[x][y] != "O":
        x += dx
        y += dy
        cnt+=1
    return x, y, cnt

def bfs():
    rr, rc, br, bc = get_pos()
    queue = deque([(rr, rc, br, bc, 1)])
    visited.append((rr, rc, br, bc))

    while queue:
        r_row, r_col, b_row, b_col, result = queue.popleft()
        if result > 10:
            break
        for i in range(4):
            nr_row, nr_col, nr_cnt = move(r_row, r_col, dx[i], dy[i])
            nb_row, nb_col, nb_cnt = move(b_row, b_col, dx[i], dy[i])
            if grid[nb_row][nb_col] == 'O':
                continue
            if grid[nr_row][nr_col] == "O":
                print(result)
                return
            if nr_row == nb_row and nr_col == nb_col:
                if nr_cnt > nb_cnt:
                    nr_row-= dx[i]
                    nr_col-= dy[i]
                else:
                    nb_row -= dx[i]
                    nb_col -= dy[i]
            if (nr_row, nr_col, nb_row, nb_col) not in visited:
                visited.append((nr_row, nr_col, nb_row, nb_col))
                queue.append((nr_row, nr_col, nb_row, nb_col, result +1))
    print(-1)
bfs()
