import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int,input().split())
start = int(input())
distances = [INF] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))  


def dijkstra(start):  
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
                heapq.heappush(queue, [distance, next_node])
    return distances

dijkstra(start)
for i in range(1, N+1):
    if distances[i] == INF:
        print("INF")
    else:
        print(distances[i])