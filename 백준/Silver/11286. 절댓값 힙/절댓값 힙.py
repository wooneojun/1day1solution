import sys
input = sys.stdin.readline

import heapq

heap = []

N = int(input())

for _ in range(N):
    num = int(input())

    if num == 0:
        if not len(heap):
            print(0)
        else:
            abs_n, n = heapq.heappop(heap)
            print(n)
    else:
        heapq.heappush(heap, (abs(num), num))