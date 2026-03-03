import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [0]*(k+1)
num_lst = set()
dp[0] = 1
for _ in range(n):
    num = int(input())
    num_lst.add(num)

for num in num_lst:
    for i in range(num, k+1):
        dp[i] += dp[i-num]
print(dp[k])