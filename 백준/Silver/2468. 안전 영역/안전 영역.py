from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(i, j, value, visited):
    q = deque()
    q.append([i, j])
    visited[i][j] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if lst[nx][ny] > value and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append([nx, ny])


n = int(input())
lst = []
hist = 0

for i in range(n):
    lst.append(list(map(int, input().split())))
    for j in range(n):
        if lst[i][j] > hist:
            hist = lst[i][j]

res = 0

for i in range(hist):
    visited = [[0] * n for i in range(n)]
    cnt = 0

    for j in range(n):
        for k in range(n):
            if lst[j][k] > i and visited[j][k] == 0:
                bfs(j, k, i, visited)
                cnt += 1
    
    if res < cnt:
        res = cnt
print(res)
