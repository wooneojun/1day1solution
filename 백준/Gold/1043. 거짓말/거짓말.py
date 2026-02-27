import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

graph = [set() for _ in range(N+1)]

true_men = list(map(int, input().split()))
tmen_set = set()


cnt = 0
party_lst = []
for _ in range(M):
    party = list(map(int, input().split()))
    party_lst.append(party[1:])
    if len(party) >2:
        for a in party[1:]:
            for b in party[1:]:
                if a != b:
                    graph[a].add(b)

for man in true_men[1:]:
    queue = deque([man])
    visited = [False]*(N+1)
    visited[man] = True
    while queue:
        m = queue.popleft()
        tmen_set.add(m)
        for t in graph[m]:
            if not visited[t]:
                visited[t] = True
                queue.append(t)

for pty in party_lst:
    flag = False
    for p in pty:
        if p in tmen_set:
            flag = True
            break
    if not flag:
        cnt += 1
print(cnt)