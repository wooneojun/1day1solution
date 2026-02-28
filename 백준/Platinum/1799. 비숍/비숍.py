import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
N = int(input())

def backtracking(idx, cnt):
    global ans
    if ans >= (cnt + L-idx):
        return
    if idx == len(bishop_pos):
        ans = max(cnt, ans)
        return
    for x, y in bishop_pos[idx]:
        if visited[x-y] == 0:
            visited[x-y] = 1
            backtracking(idx+1, cnt+1)
            visited[x-y] = 0
    backtracking(idx+1, cnt)

grid = []
L = 2*N-1
bishop_pos = [[] for _ in range(L)]
ans = 0
visited = [0]*L
for i in range(N):
    row = list(map(int, input().split()))
    grid.append(row)
    for j in range(N):
        if row[j] == 1:
            bishop_pos[i+j].append((i, j))
backtracking(0, 0)
print(ans)
