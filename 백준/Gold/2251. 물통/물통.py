from collections import deque

a, b, c = map(int, input().split())

q = deque()
q.append((0, 0))

visited = [[False] * (b + 1) for _ in range(a + 1)]
visited[0][0] = True

answer = []

def pour (x, y):
    if not visited[x][y]:
        visited[x][y] = True
        q.append((x, y))

def bfs():
    while q:
        x, y = q.popleft()
        z = c - x - y

        if x == 0:
            answer.append(z)
        # A>B
        water = min(x, b - y)
        pour(x - water, y + water)
        # A>C
        water = min(x, c -z)
        pour(x - water, y)

        # B>C
        water = min(y, c - z)
        pour(x , y - water)
        # B>A
        water = min(y, a - x)
        pour(x + water, y - water)

        # C>A
        water = min(z, a - x)
        pour(x + water, y)
        # C>B
        water = min(z, b - y)
        pour(x, y + water)

bfs()

answer.sort()
for i in answer:
    print(i, end = " ")
    