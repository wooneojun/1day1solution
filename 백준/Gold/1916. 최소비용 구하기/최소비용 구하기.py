import heapq
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
costs = [10**8]*(n+1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

start, end = map(int, input().split())
costs[start] = 0
heap = [[0, start]]
while heap:
    cur_cost, cur_node = heapq.heappop(heap)
    if cur_cost > costs[cur_node]:
        continue
    for next_node, next_cost in graph[cur_node]:
        next_num = cur_cost + next_cost
        if next_num <costs[next_node]:
            costs[next_node] = next_num
            heapq.heappush(heap, [next_num, next_node])
print(costs[end])
