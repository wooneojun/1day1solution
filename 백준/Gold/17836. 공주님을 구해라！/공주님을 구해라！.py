import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M, T = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(N)]


def find(row, col):
    visited = [[-1]*M for _ in range(N)]
    visited[0][0] = 0

    queue = deque([(0,0)])
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            if 0<=nr<N and 0<=nc<M and visited[nr][nc] == -1:
                if grid[nr][nc] != 1:
                    visited[nr][nc] = visited[r][c] + 1
                    queue.append((nr, nc))
    return visited[row][col]


for row in range(N):
    for col in range(M):
        if grid[row][col] == 2:
            sword = (row, col)

# 검 안찾고 가는 방법
no_sword = find(N-1, M-1)
flag = False
if no_sword == -1:
    flag = True

# 검 찾고 가는 방법
yes_sword = find(sword[0], sword[1])
y_flag = False
if yes_sword == -1:
    y_flag = True
if not y_flag:
    yes_sword += N-1-sword[0]+M-1-sword[1]

if flag and y_flag:
    print("Fail")
elif flag and not y_flag:
    if yes_sword <= T:
        print(yes_sword)
    else:
        print("Fail")
elif not flag and y_flag:
    if no_sword <= T:
        print(no_sword)
    else:
        print("Fail")
else:
    s = min(no_sword, yes_sword)
    if s <= T:
        print(s)
    else:
        print("Fail")