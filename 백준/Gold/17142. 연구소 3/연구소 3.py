import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
grid = []
virus_all = []
empty_count = 0

for r in range(N):
    row = list(map(int, input().split()))
    grid.append(row)
    for c in range(N):
        if row[c] == 2:
            virus_all.append((r, c))
        elif row[c] == 0:
            empty_count += 1

# 처음 빈 칸이 없으면 0초
if empty_count == 0:
    print(0)
    exit()

v_pos = combinations(virus_all, M)
ans = 10**8

for pos in v_pos:
    visit = [[-1] * N for _ in range(N)]
    queue = deque()
    for r, c in pos:
        visit[r][c] = 0
        queue.append((r, c))
    
    cnt = 0 # 이번 턴에 채운 빈 칸 개수
    max_time = 0
    
    while queue:
        r, c = queue.popleft()
        
        for i in range(4):
            nr, nc = r + dx[i], c + dy[i]
            
            if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] != 1 and visit[nr][nc] == -1:
                visit[nr][nc] = visit[r][c] + 1
                queue.append((nr, nc))
                
                # 빈 칸을 만났을 때만 시간과 개수 업데이트
                if grid[nr][nc] == 0:
                    cnt += 1
                    max_time = visit[nr][nc]
        
    # 모든 빈 칸을 다 채웠다면 최솟값 갱신
    if cnt == empty_count:
        ans = min(ans, max_time)

print(ans if ans != 10**8 else -1)