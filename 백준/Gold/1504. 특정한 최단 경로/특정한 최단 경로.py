import sys
import heapq

input = sys.stdin.readline
INF = float('inf')

# 1. 입력 받기
N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]

# 양방향 그래프 구성
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

# 2. 다익스트라 함수 정의
def dijkstra(start):
    distances = [INF] * (N + 1)
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        
        # 이미 처리된 노드라면 무시 (가지치기)
        if distances[current_node] < current_dist:
            continue
            
        for next_node, weight in graph[current_node]:
            distance = current_dist + weight
            
            # 더 짧은 경로를 찾았다면 갱신하고 큐에 넣기
            if distance < distances[next_node]:
                distances[next_node] = distance
                heapq.heappush(pq, (distance, next_node))
                
    return distances

# 3. 다익스트라 3번 실행 (각각 1, v1, v2에서 출발하는 모든 최단 거리)
dist_from_1 = dijkstra(1)
dist_from_v1 = dijkstra(v1)
dist_from_v2 = dijkstra(v2)

# 4. 두 가지 시나리오의 거리 계산
# 시나리오 A: 1 -> v1 -> v2 -> N
path1 = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[N]

# 시나리오 B: 1 -> v2 -> v1 -> N
path2 = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[N]

# 5. 최솟값 찾기 및 예외 처리
result = min(path1, path2)

# 만약 경로가 아예 없어서 무한대(INF) 값이 섞여 있다면 도달 불가능한 것
if result >= INF:
    print(-1)
else:
    print(result)