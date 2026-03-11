import sys
import heapq

input = sys.stdin.readline

N = int(input())
lectures = []
for _ in range(N):
    lectures.append(list(map(int, input().split())))

lectures.sort()

room = []
heapq.heappush(room, lectures[0][1])

for i in range(1, N):
    if lectures[i][0] >= room[0]:
        heapq.heappop(room)
        heapq.heappush(room, lectures[i][1])
    else:
        heapq.heappush(room, lectures[i][1])

print(len(room))