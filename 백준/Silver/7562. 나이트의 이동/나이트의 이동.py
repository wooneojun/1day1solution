from collections import deque
import sys

def bfs():
    q = deque()
    
    dx = [-1, -1, -2, -2, 1, 1, 2, 2]
    dy = [2, -2, 1, -1, 2, -2, 1, -1]

    q.append((sx, sy))
    while q:
        x, y = q.popleft()
        if x == ex and y == ey:
            return chess[x][y] - 1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= w or ny < 0 or ny >=w:
                continue
            if chess[nx][ny] == 0:
                chess[nx][ny] = chess[x][y] + 1
                q.append((nx, ny))

input = sys.stdin.readline
n = int(input())
for _ in range(n):
    w = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    chess = [[0] * w for _ in range(w)]
    chess[sx][sy] = 1
    print(bfs())
