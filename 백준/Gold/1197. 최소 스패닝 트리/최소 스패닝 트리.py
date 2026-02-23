import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
V, E = map(int, input().split())

def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_find(parent, a, b):
    root_a = find_parent(parent, a)
    root_b = find_parent(parent, b)
    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b
lst = []
for _ in range(E):
    a, b, cost = map(int, input().split())
    lst.append((cost, a, b))
lst.sort()

parent = [i for i in range(V+1)]
ans = 0
for cost, a, b in lst:
    if find_parent(parent, a) != find_parent(parent, b):
        union_find(parent, a, b)
        ans += cost
print(ans)