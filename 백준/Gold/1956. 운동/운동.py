import sys
input = sys.stdin.readline

INF = int(1e9)
N, M = map(int, input().split())
graph = [[INF]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    
ans = INF
for i in range(1, N+1):
    ans = min(ans, graph[i][i])
if ans == INF:
    print(-1)
else:
    print(ans)