def def_sqr(s):
    for i in range(n - s + 1):
        for j in range(m - s + 1):
            if lst[i][j] == lst[i][j + s - 1] == lst[i + s - 1][j] == lst[i + s - 1][j + s -1]:
                return True

n, m = map(int, input().split())
lst = []
lst = [list(map(int,list(input()))) for _ in range(n)]

size = min(n, m)

for k in range(size, 0, -1):
    if def_sqr(k):
        print(k ** 2)
        break