import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N = int(input())

def find_island(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    grid[x][y] = num
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nx, ny = r + dx[i], c + dy[i]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and grid[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True
                grid[nx][ny] = num

def bfs(island):
    q = deque()
    dist = [[-1] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if grid[i][j] == island:
                q.append((i, j))
                dist[i][j] = 0
                
    while q:
        x, y = q.popleft()
 
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < N and 0 <= ny < N:
                if grid[nx][ny] != island and grid[nx][ny] != 0: 
                    return dist[x][y]
                if grid[nx][ny] == 0 and dist[nx][ny] == -1: 
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    return 10**8

grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]

num = 1
for i in range(N):
    for j in range(N):
        if grid[i][j] == 1 and not visited[i][j]:
            find_island(i, j)
            num += 1

result = 10**8
for island in range(1, num):
    result = min(result, bfs(island))

print(result)