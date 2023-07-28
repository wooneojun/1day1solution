n = int(input())
lst = []
ans = []
for _ in range(n):
    a, b = map(int, input().split())
    lst.append([a, b])

dp = [0 for _ in range(n + 1)]
for i in range(n):
    for j in range(i + lst[i][0], n+1):
        if dp[j] < dp[i] + lst[i][1]:
            dp[j] = dp[i] + lst[i][1]

print(dp[-1])
