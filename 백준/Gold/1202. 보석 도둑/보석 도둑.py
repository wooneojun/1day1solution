import sys, heapq
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

heap = []

for _ in range(N):
    m, v = map(int, input().split())
    heapq.heappush(heap, (m, v))

bag = [int(input()) for _ in range(K)]
bag.sort()
value_heap = []
ans = 0
for b in bag:
    while heap and b>= heap[0][0]:
        m, v = heapq.heappop(heap)
        heapq.heappush(value_heap, -v)
    if value_heap:
        ans-= heapq.heappop(value_heap)

print(ans)
