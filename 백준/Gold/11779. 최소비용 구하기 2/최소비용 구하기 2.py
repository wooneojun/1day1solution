import heapq
import sys
input = sys.stdin.readline

N = int(input())  
M = int(input())  
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))  
start, end = map(int, input().split())
lst = [0] * (N+1)

def dijkstra(graph, start):
    distances = [int(1e9)] * (N+1)
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        dist, node = heapq.heappop(queue)

        if distances[node] < dist:
            continue

        for next_node, next_dist in graph[node]:
            distance = dist + next_dist
            if distance < distances[next_node]:
                distances[next_node] = distance
                lst[next_node] = node
                heapq.heappush(queue, [distance, next_node])
    return distances

dist_start = dijkstra(graph, start)
print(dist_start[end])
path = []
curr = end
while curr:
    path.append(curr)
    curr = lst[curr]
print(len(path))
for i in path[::-1]:
    print(i, end=" ")