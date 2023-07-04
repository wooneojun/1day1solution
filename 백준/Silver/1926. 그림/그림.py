from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(i, j, pic):
    q = deque([[i, j]])
    pic[i][j] = 2
    result = 1

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<n and 0<=ny<m and pic[nx][ny] == 1:
                q.append([nx,ny])
                pic[nx][ny] = 2
                result += 1
    return result

n, m = map(int, input().split())
lst = []
answer = 0
cnt = 0

for _ in range(n):
    lst.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if lst[i][j] == 1:
            ans = bfs(i, j, lst)
            answer = max(ans, answer)
            cnt += 1
print(cnt)
print(answer)
