import sys
input = sys.stdin.readline

import heapq

heap = []

N = int(input())

for _ in range(N):
    num = int(input())
    heapq.heappush(heap, num)
cnt = 0
while len(heap) >1:
    a, b = heapq.heappop(heap), heapq.heappop(heap)
    cnt += a+b
    heapq.heappush(heap, a+b)

print(cnt)