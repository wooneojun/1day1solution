import sys
input = sys.stdin.readline
from collections import deque

#     북 동 남 서   -인 경우 반시계
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
r, c, d = map(int, input().split())
queue = deque([(r, c, d)])
clean = [[0]*M for _ in range(N)]
grid = [list(map(int, input().split())) for _ in range(N)]

while queue:
    row, col, direction = queue.popleft()
    clean[row][col] = 1
    flag = False
    # 청소되지 않은 빈칸이 있는 경우를 찾아야함
    for i in range(4):
        n_row = row + dx[i]
        n_col = col + dy[i]
        if grid[n_row][n_col] == 0 and not clean[n_row][n_col]:
            flag = True
            break
    # 청소되지 않은 빈칸이 없는 경우
    if not flag:
        if grid[row+dx[direction-2]][col+dy[direction-2]]==1:
            break
        else:
            queue.append((row+dx[direction-2], col+dy[direction-2], direction))
    else:
        for j in range(4):
            direction = (direction-1) % 4
            if grid[row+dx[direction]][col+dy[direction]] == 0 and not clean[row+dx[direction]][col+dy[direction]]:
                queue.append((row+dx[direction], col+dy[direction], direction))
                break

cnt= 0
for row in clean:
    cnt += sum(row)
print(cnt)
