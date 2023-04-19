import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
n_lst = [0 for _ in range(n)]
cnt = 0
for i in lst:
    k = 0
    flag = i
    cnt += 1
    while flag > 0 or n_lst[k]!=0:
        if n_lst[k] == 0:
            flag -= 1
        k += 1
    n_lst[k] = cnt
print(" ".join(map(str, n_lst)))