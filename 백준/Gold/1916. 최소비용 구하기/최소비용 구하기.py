import heapq
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])

start, end = map(int, input().split())

costs = [10**8 for _ in range(n+1)]
heap = []
costs[start] = 0
heapq.heappush(heap, [0, start])
while heap:
    cur_cost, cur_node = heapq.heappop(heap)
    if costs[cur_node] < cur_cost:
        continue
    for next_node, next_cost in graph[cur_node]:
        sum_cost = cur_cost + next_cost
        if sum_cost >= costs[next_node]:
            continue

        costs[next_node] = sum_cost
        heapq.heappush(heap, [sum_cost, next_node])
print(costs[end])
