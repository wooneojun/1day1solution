import sys
input = sys.stdin.readline
from collections import deque

def bfs(a, lst):
    visited = [False] *(N+1)
    visited[a] = True
    queue = deque([a])
    cnt = 0
    while queue:
        q = queue.popleft()
        for b in lst[q]:
            if not visited[b]:
                visited[b] = True
                cnt +=1
                queue.append(b)
    return cnt

def find_pos(a):
    ans = bfs(a, upper_list)
    ans += bfs(a, lower_list)
    if ans == N-1:
        return 1
    return 0

N, M = map(int, input().split())
upper_list = [[] for _ in range(N+1)]
lower_list = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    upper_list[a].append(b)
    lower_list[b].append(a)
answer = 0
for i in range(1, N+1):
    answer += find_pos(i)
print(answer)
