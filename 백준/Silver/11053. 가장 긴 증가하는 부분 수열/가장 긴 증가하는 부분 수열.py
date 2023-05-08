import sys
input = sys.stdin.readline

n = int(input())
n_lst = list(map(int, input().split()))
cnt = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(0, i):
        if n_lst[j] < n_lst[i]:
            cnt[i] = max(cnt[i], cnt[j] + 1)
print(max(cnt))