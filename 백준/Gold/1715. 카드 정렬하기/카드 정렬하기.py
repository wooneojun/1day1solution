import sys
import heapq
input = sys.stdin.readline
heap = []
lst = []
N = int(input())
for _ in range(N):
    heapq.heappush(heap, int(input()))
for i in range(N-1):
    pls = heapq.heappop(heap) + heapq.heappop(heap)
    lst.append(pls)
    heapq.heappush(heap, pls)
if N == 1:
    print(0)
else:
    print(sum(lst))