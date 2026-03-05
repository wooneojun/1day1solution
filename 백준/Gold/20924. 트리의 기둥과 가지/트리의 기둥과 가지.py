import sys
from collections import deque
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
N, R = map(int, input().split())

def dfs(node, cnt):
    visited[node] = True
    if len(giga_node[node])==1:
        global ans
        ans = max(ans, cnt)
        return
    for n, e in giga_node[node]:
        if not visited[n]:
            dfs(n, cnt+e)

giga_node = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(N-1):
    a, b, e = map(int, input().split())

    giga_node[a].append((b, e))
    giga_node[b].append((a, e))

visited[R] = True
queue = deque([R])
column = 0
giga = R
leaf_flag = False
if len(giga_node[R]) == 1:
    while queue:
        node = queue.popleft()
        giga = node
        if len(giga_node[node])>2:
            break
        for n, e in giga_node[node]:
            if not visited[n]:
                visited[n] = True
                column += e
                queue.append(n)
ans = 0

dfs(giga, 0)
print(f"{column} {ans}")


