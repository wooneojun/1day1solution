import sys
input = sys.stdin.readline
import heapq

T = int(input())

for tc in range(1, 1+T):
    cross, road, target = map(int, input().split())
    start, cand1, cand2 = map(int, input().split())
    
    target_node = []
    roads = [{} for _ in range(cross + 1)]
    
    # 그래프 연결
    for _ in range(road):
        a, b, d = map(int, input().split())
        if not roads[a].get(b, 0):
            roads[a][b] = d
            roads[b][a] = d
        else:
            roads[a][b] = min(roads[a][b], d)
            roads[b][a] = roads[a][b]
            
    for _ in range(target):
        t = int(input())
        target_node.append(t)


    def get_dist(start_node):
        # 거릿값 저장 리스트
        dist = [10**8] * (cross + 1)
        dist[start_node] = 0
        heap = [(0, start_node)]
        
        while heap:
            edge, node = heapq.heappop(heap)
            
            # 큐에서 꺼낸 거리가 이미 기록된 최단 거리보다 멀면 무시
            if dist[node] < edge:
                continue
                
            for n_node, n_edge in roads[node].items():
                new_edge = edge + n_edge
                # 더 짧은 경로를 발견했을 때만 갱신하고 큐에 넣음
                if new_edge < dist[n_node]:
                    dist[n_node] = new_edge
                    heapq.heappush(heap, (new_edge, n_node))
        return dist

    # 함수 3번 호출로 필요한 모든 최단 거리 확보
    dist_start = get_dist(start)
    dist_cand1 = get_dist(cand1)
    dist_cand2 = get_dist(cand2)
     
    # 누락되었던 cand1과 cand2 사이의 실제 거리
    mid_dist = roads[cand1][cand2]
    
    # 각각 절대적 최단거리인지 확인
    ans = []
    for t in target_node:
        original_shortest = dist_start[t] # 그냥 갔을 때 최단 거리
        
        # start - cand1 - cand2 - target
        path1 = dist_start[cand1] + mid_dist + dist_cand2[t]
        # start - cand2 - cand1 - target
        path2 = dist_start[cand2] + mid_dist + dist_cand1[t]
        
        # 후보 교차로를 거쳐간 경로가 진짜 최단 거리와 일치한다면 정답!
        if original_shortest == path1 or original_shortest == path2:
            ans.append(t)

    ans.sort()
    for a in ans:
        print(a, end=" ")
    print()