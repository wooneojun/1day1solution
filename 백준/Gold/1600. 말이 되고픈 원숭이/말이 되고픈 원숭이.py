import sys
from collections import deque
input = sys.stdin.readline

dmx = [1, -1, 0, 0]
dmy = [0, 0, 1, -1]
dhx = [2, 2, -2, -2, 1, 1, -1, -1]
dhy = [-1, 1, -1, 1, 2, -2, 2, -2]

K = int(input())
W, H = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(H)]

visited = [[[False] * (K + 1) for _ in range(W)] for _ in range(H)]
visited[0][0][K] = True

queue = deque([(0, 0, K, 0)])
ans = -1

while queue:
    row, col, horse, cnt = queue.popleft()
    
    if row == H - 1 and col == W - 1:
        ans = cnt
        break
        
    if horse > 0:
        for i in range(8):
            nx, ny = row + dhx[i], col + dhy[i]
            if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] == 0:
                if not visited[nx][ny][horse - 1]:
                    visited[nx][ny][horse - 1] = True
                    queue.append((nx, ny, horse - 1, cnt + 1))

    for i in range(4):
        nx, ny = row + dmx[i], col + dmy[i]
        if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] == 0:
            if not visited[nx][ny][horse]:
                visited[nx][ny][horse] = True
                queue.append((nx, ny, horse, cnt + 1))

print(ans)