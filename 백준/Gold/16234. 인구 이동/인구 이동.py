from collections import deque
import sys
input = sys.stdin.readline

dx, dy = [0,1,0,-1], [1, 0, -1, 0]

def bfs():
    visited = [[False]*N for _ in range(N)]
    flag = False
    for row in range(N):
        for col in range(N):
            if not visited[row][col]:
                visited[row][col] = True
                queue = deque([(row, col)])
                tmp_lst = [grid[row][col]]
                tmp_pos = [(row, col)]
                while queue:
                    r, c= queue.popleft()
                    for i in range(4):
                        nr, nc = r + dx[i], c + dy[i]
                        if 0<=nr<N and 0<=nc<N and not visited[nr][nc]:
                            if L<=abs(grid[nr][nc] - grid[r][c])<=R:
                                tmp_lst.append(grid[nr][nc])
                                tmp_pos.append((nr, nc))
                                queue.append((nr, nc))
                                visited[nr][nc] = True
                if len(tmp_lst) >1:
                    flag = True
                    for r, c in tmp_pos:
                        grid[r][c] = sum(tmp_lst)//len(tmp_lst)
    return flag


N, L, R = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
while True:
    if bfs():
        cnt += 1
    else:
        break

print(cnt)