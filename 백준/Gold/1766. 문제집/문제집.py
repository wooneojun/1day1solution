import sys, heapq
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
suffix = [0] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    suffix[b] += 1

queue = []
for idx in range(1, N+1):
    if suffix[idx] == 0:
        heapq.heappush(queue, idx)
ans = []
while queue:
    idx = heapq.heappop(queue)
    ans.append(idx)
    for i in graph[idx]:
        suffix[i] -= 1
        if suffix[i] == 0:
            heapq.heappush(queue, i)
print(*ans)