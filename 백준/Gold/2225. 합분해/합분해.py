N, K = map(int, input().split())
lst = [[0] * 201 for _ in range(201)]
for i in range(201):
    lst[1][i] = i
    lst[i][1] = 1

for k in range(2, 201):
    for j in range(2, 201):
        lst[k][j] = (lst[k - 1][j] + lst[k][j - 1]) % 1000000000

print(lst[N][K])