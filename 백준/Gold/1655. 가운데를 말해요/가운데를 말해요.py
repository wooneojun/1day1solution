import sys
import heapq

input = sys.stdin.readline

N = int(input())
max_h = [] # 중간값보다 작은 값들 
min_h = [] # 중간값보다 큰 값들

for _ in range(N):
    num = int(input())

    if len(max_h) == len(min_h):
        heapq.heappush(max_h, -num)
    else:
        heapq.heappush(min_h, num)

    if min_h and -max_h[0] > min_h[0]:
        max_val = -heapq.heappop(max_h)
        min_val = heapq.heappop(min_h)

        heapq.heappush(max_h, -min_val)
        heapq.heappush(min_h, max_val)

    print(-max_h[0])