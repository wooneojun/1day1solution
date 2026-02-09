"""
Docstring for 3번 줄기세포 배양

시간의 흐름에 따라 가야할거 같은데 일단 받았던 애들 힙에 다 집어넣고 시작

def 배양 (살아있는애들 담은 리스트, 시간)
큐 한번 싹 돌리는데 (health, x, y, remaining_time, is_activate)

맨첨에


일단 칸을 차지하기만 하면 칸 세트에 넣어두고
죽은애들은 그냥 무시
살아있는 애들은 힙 큐에 넣자
"""
 
import heapq
from copy import deepcopy

T = int(input())
direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
for tc in range(1, T+1):
    grid = []
    heap = []
    remaining_pos = set()

    N, M, K = map(int, input().split())

    for _ in range(N):
        grid.append(list(map(int, input().split())))
    
    for row in range(N):
        for col in range(M):
            val = grid[row][col]
            if val>0:
                heapq.heappush(heap, (-val, row, col, 0, False))
                remaining_pos.add((row, col))
    
    for times in range(K):
        # 힙을 갱신해줄 기준 힙
        temp_heap = []
        while heap:
            negative_val, row, col, remaining_time, is_activate = heapq.heappop(heap)
            # 1. 만약 r_time == 0이고 is_activate == True 면
            if remaining_time == 0 and is_activate:
                # 상하좌우 탐색해서 remaining_pos에 없으면 remaining_pos 에 넣고 큐에 ((val, row, next_col, 0, True))
                for i in range(4):
                    n_row, n_col = row + direction[i][0], col + direction[i][1]
                    if (n_row, n_col) not in remaining_pos:
                        remaining_pos.add((n_row,n_col))
                        heapq.heappush(temp_heap, (negative_val, n_row, n_col, 0, False))
                    # (val, row, col, 1, True) 큐에 넣음
                if -negative_val > 1:
                    heapq.heappush(temp_heap, (negative_val, row, col, remaining_time + 1, True))
                continue
            # 2. remaining_time += 1
            if not is_activate:
                if remaining_time + 1 == -negative_val:
                    heapq.heappush(temp_heap, (negative_val, row, col, 0, True))
                else:
                    # 아직 비활성 시간 남음
                    heapq.heappush(temp_heap, (negative_val, row, col, remaining_time + 1, False))
            else:
                # 활성 상태 시간이 생명력보다 작으면 생존
                if remaining_time + 1 < -negative_val:
                    heapq.heappush(temp_heap, (negative_val, row, col, remaining_time + 1, True))
            
        heap = temp_heap
    print(f"#{tc} {len(heap)}")
            
