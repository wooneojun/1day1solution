import heapq
import sys

input = sys.stdin.readline
n = int(input())
num = []

for _ in range(n):
    num.append(list(map(int, input().split())))
num.sort()
room = []
heapq.heappush(room, num[0][1])
num.remove(num[0])

for i, j in num:
    small = heapq.heappop(room)
    if small <= i:
        heapq.heappush(room, j)
    else:
        heapq.heappush(room, small)
        heapq.heappush(room, j)

print(len(room))