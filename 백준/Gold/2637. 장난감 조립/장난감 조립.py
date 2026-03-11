import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
M = int(input())

dd = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
is_basic = [True]*(N+1)

for _ in range(M):
    X, Y, K = map(int, input().split())
    dd[X].append((Y, K))
    indegree[Y] += 1
    is_basic[X] = False

lst = [0]*(N+1)
lst[N] = 1
queue = deque([N])

while queue:
    curr = queue.popleft()

    for child, need_count in dd[curr]:
        lst[child] += lst[curr] * need_count
        indegree[child] -= 1

        if indegree[child] == 0:
            queue.append(child)

for i in range(1, N + 1):
    if is_basic[i]:
        print(i, lst[i])