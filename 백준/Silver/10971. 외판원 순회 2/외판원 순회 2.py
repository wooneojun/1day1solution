import sys

def tsp(start, cur, visited, cost):
    global min_cost
    if sum(visited) == n:
        if w[cur][start] != 0:
            min_cost = min(min_cost, cost + w[cur][start])
        return

    for i in range(n):
        if not visited[i] and w[cur][i] != 0:
            visited[i] = True
            tsp(start, i, visited, cost + w[cur][i])
            visited[i] = False

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
min_cost = sys.maxsize
flag = [1] + [0 for _ in range(n-1)]
for i in range(n):
    visited = [False for _ in range(n)]
    visited[i] = True
    tsp(i, i, visited, 0)

print(min_cost)