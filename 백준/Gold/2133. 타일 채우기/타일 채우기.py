from collections import defaultdict
import sys

input = sys.stdin.readline

n = int(input())

dp = defaultdict(int)
dp[2] = 3
for i in range(4, n + 1):
    if i % 2 == 0:
        dp[i] = dp[i-2] * 3 + (sum(dp.values()) - dp[i-2]) * 2 + 2
print(dp[n])