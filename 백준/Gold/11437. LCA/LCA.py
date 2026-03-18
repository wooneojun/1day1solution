import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

graph =[[] for _ in range(N+1)]
parent = [0] * (N+1)
parent[1] = 0
levels = [10**8] * (N+1)
levels[1] = 0
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] *(N+1)

visited[1] = True

queue = deque([(1, 0)])
while queue:
    ans, level = queue.popleft()
    for node in graph[ans]:
        if not visited[node]:
            visited[node] = True
            parent[node] = ans
            levels[node] = level + 1
            queue.append((node, level+1))

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())

    if levels[a]>levels[b]:
        tmp = a
        a = b
        b = tmp
    while levels[a]!= levels[b]:
        b = parent[b]
    while a != b:
        a = parent[a]
        b = parent[b]
    print(a)