import sys
input = sys.stdin.readline

lst = list(map(int, input().rstrip()))
l = len(lst)

dp = [0] * (l+1)
dp[0] = 1 #1번 인덱스 1자리수 구할때 필요
dp[1] = 1
if lst[0] == 0:
    print(0)
else:
    for k in range(1, l):
        i = k+1
        if lst[k] >0:
            dp[i] += dp[i-1]
        if 10<=lst[k]+lst[k-1]*10<=26:
            dp[i] += dp[i-2]
    print(dp[l]%1000000)