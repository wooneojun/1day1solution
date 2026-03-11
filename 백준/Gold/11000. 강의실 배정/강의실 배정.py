import sys
import heapq

input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort()
heap = [lst[0][1]]
for i in range(1, N):
    if heap[0]<=lst[i][0]:
        heapq.heappop(heap)
    heapq.heappush(heap, lst[i][1])
print(len(heap))