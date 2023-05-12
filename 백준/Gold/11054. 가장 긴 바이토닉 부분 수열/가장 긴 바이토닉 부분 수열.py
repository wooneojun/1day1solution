n = int(input())
dp = list(map(int, input().split()))
up_dp = [1 for _ in range(n)]
dn_dp = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(0, i):
        if dp[j] < dp[i]:
            up_dp[i] = max(up_dp[i], up_dp[j] + 1)

if n > 1:
    for i in range(n-2, -1, -1):
        for j in range(n-1, i-1, -1):
            if dp[j] < dp[i]:
                dn_dp[i] = max(dn_dp[i], dn_dp[j] + 1)

for i in range(n):
    dp[i] = up_dp[i] + dn_dp[i] - 1

print(max(dp))