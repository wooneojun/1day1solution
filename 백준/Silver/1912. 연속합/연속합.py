import sys
input = sys.stdin.readline

n = int(input())
n_lst = list(map(int, input().split()))
for i in range(1, n):
    if n_lst[i-1] > 0:
        n_lst[i] = n_lst[i-1] + n_lst[i]
print(max(n_lst))