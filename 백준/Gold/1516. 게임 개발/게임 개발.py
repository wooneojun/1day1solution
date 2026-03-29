import sys
import heapq

input = sys.stdin.readline
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * (N+1)
link = [[] for _ in range(N+1)]

for i in range(N):
    for j in range(1, len(lst[i])):
        if lst[i][j] == -1:
            break
        link[lst[i][j]].append(i+1)
        visited[i+1] += 1

heap = []

for i in range(1, N+1):
    if visited[i]==0:
        heapq.heappush(heap, (0, i))

leng_lst = [0]*(N+1)
max_time = [0] * (N+1) 

while heap:
    length, node = heapq.heappop(heap)
    
    length += lst[node-1][0] 
    leng_lst[node] = length
    
    for i in link[node]:
        visited[i] -= 1
        max_time[i] = max(max_time[i], length)
        
        if visited[i] == 0:
            heapq.heappush(heap, (max_time[i], i))

for i in range(1, N+1):
    print(leng_lst[i])