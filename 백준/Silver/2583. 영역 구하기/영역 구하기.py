from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(i, j):
    q = deque()
    q.append([i, j])
    cnt = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<M and 0<=ny<N:
                if lst[nx][ny] == 0:
                    lst[nx][ny] = 1
                    q.append([nx, ny])
                    cnt += 1
    return cnt

M, N, K = map(int, input().split())
lst = [[0]*N for _ in range(M)]

for _ in range(K):
    fx, fy, lx, ly = map(int, input().split())
    for i in range(fx, lx):
        for j in range(fy, ly):
            lst[j][i] = 1
res = []
for i in range(M):
    for j in range(N):
        if lst[i][j] == 0:
            lst[i][j] = 1
            res.append(bfs(i, j))
res.sort()
print(len(res))
print(*res)