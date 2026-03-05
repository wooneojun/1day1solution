import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

# 초기 상어 위치 찾기 및 빈칸 처리
for r in range(N):
    for c in range(N):
        if grid[r][c] == 9:
            shark_row, shark_col = r, c
            grid[r][c] = 0

shark_size = 2
shark_eaten = 0
total_time = 0

# 상어 위치에서 먹을 수 있는 가장 가까운 물고기 찾는 BFS
def find_fish(s_row, s_col, s_size):
    queue = deque([(s_row, s_col, 0)])
    visited = [[False] * N for _ in range(N)]
    visited[s_row][s_col] = True
    
    candidates = [] # 먹을 수 있는 물고기들을 담을 리스트
    
    while queue:
        r, c, dist = queue.popleft()
        
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if grid[nr][nc] <= s_size: # 지나갈 수 있는 경우
                    visited[nr][nc] = True
                    # 먹을 수 있는 물고기인 경우 (빈칸 0 제외)
                    if 0 < grid[nr][nc] < s_size:
                        candidates.append((dist + 1, nr, nc))
                    else:
                        queue.append((nr, nc, dist + 1))
    
    # 거리, 위쪽(row), 왼쪽(col) 순으로 정렬하여 가장 우선순위 높은 것 반환
    if not candidates:
        return None
    candidates.sort()
    return candidates[0]

while True:
    # 1. 현재 위치에서 먹을 물고기 탐색
    result = find_fish(shark_row, shark_col, shark_size)
    
    # 2. 더 이상 먹을 물고기가 없으면 종료
    if result is None:
        break
    
    dist, f_row, f_col = result
    
    # 3. 물고기 먹기 처리
    total_time += dist
    shark_row, shark_col = f_row, f_col
    grid[f_row][f_col] = 0 # 먹었으니 빈칸
    
    shark_eaten += 1
    if shark_eaten == shark_size:
        shark_size += 1
        shark_eaten = 0

print(total_time)