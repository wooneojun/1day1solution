import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
LOG = 21 # 2^20 = 1,048,576 (N의 최대치보다 충분히 큰 2의 제곱수 지수)

# 1. 트리 연결 리스트
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# parent[i][j] = i번 노드의 2^j 번째 위(부모) 조상
parent = [[0] * LOG for _ in range(N + 1)]
depth = [0] * (N + 1)
visited = [False] * (N + 1)

# 2. BFS로 바로 위 부모(2^0)와 깊이(depth) 기록
def bfs(root):
    queue = deque([root])
    visited[root] = True
    depth[root] = 0
    
    while queue:
        curr = queue.popleft()
        for nxt in graph[curr]:
            if not visited[nxt]:
                visited[nxt] = True
                parent[nxt][0] = curr # 바로 위 부모 기록
                depth[nxt] = depth[curr] + 1
                queue.append(nxt)

# 3. DP를 이용해 2^j 번째 부모 정보 채우기
def set_parent():
    bfs(1) # 1번을 루트로 트리 구성
    for i in range(1, LOG):
        for j in range(1, N + 1):
            # j의 2^i 번째 부모는, j의 2^(i-1) 번째 부모의 2^(i-1) 번째 부모와 같음
            parent[j][i] = parent[parent[j][i - 1]][i - 1]

# 4. 공통 조상을 찾는 함수 (O(log N))
def lca(a, b):
    # 항상 b가 더 깊도록 스왑
    if depth[a] > depth[b]:
        a, b = b, a
        
    # 1단계: a와 b의 깊이를 맞춘다 (b를 위로 끌어올림)
    # 차이가 나는 만큼 2의 제곱수로 점프
    for i in range(LOG - 1, -1, -1):
        if depth[b] - depth[a] >= (1 << i):
            b = parent[b][i]
            
    # 깊이를 맞췄는데 두 노드가 같아졌다면 그것이 LCA
    if a == b:
        return a
        
    # 2단계: 공통 조상 바로 아래까지 동시에 점프하며 올라감
    for i in range(LOG - 1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
            
    # 현재 a, b는 공통 조상 바로 아래에 있으므로, a의 바로 위 부모가 정답
    return parent[a][0]

set_parent()

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(lca(a, b))