import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for tc in range(T):
    N = int(input())
    graph = [[] for _ in range(N + 1)]
    parent = [0] * (N+1)
    nodes = [False] *(N+1)
    for _ in range(N-1):
        a, b = map(int, input().split())
        nodes[b] = True
        graph[a].append(b)
        parent[b] = a

    root = 0
    for i in range(1, N+1):
        if not nodes[i]:
            root = i
            break
    
    levels = [0] * (N+1)
    queue = deque([(root, 0)])
    while queue:
        cur_node, level = queue.popleft()
        for node in graph[cur_node]:
            levels[node] = level + 1
            queue.append((node, level + 1))
    a, b = map(int, input().split())

    # 무조건 a 가 더 위에 있게
    if levels[a] > levels[b]:
        tmp = a
        a = b
        b = tmp
    
    while levels[a] != levels[b]:
        b = parent[b]
    
    while a != b:
        a = parent[a]
        b = parent[b]
    print(a)
    
    
