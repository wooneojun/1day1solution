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

for i in range(1, n):
    if num[i][0] < room[0]:
        heapq.heappush(room, num[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, num[i][1])

print(len(room))