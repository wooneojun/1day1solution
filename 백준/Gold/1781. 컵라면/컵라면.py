import sys
import heapq
input = sys.stdin.readline

N = int(input())
problems = [list(map(int, input().split())) for _ in range(N)]
problems.sort()
queue = []
for deadline, cupRamen in problems:
    heapq.heappush(queue, cupRamen)
    if deadline < len(queue):
        heapq.heappop(queue)
print(sum(queue))