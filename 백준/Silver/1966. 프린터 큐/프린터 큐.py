import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    n, m = map(int, input().split())
    n_lst = list(map(int, input().split()))
    idx_lst = [[item, i] for i, item in enumerate(n_lst)]
    flag = True
    cnt = 0
    while flag:
        max_n = max(idx_lst)[0]
        item = idx_lst.pop(0)
        if item[0] != max_n:
            idx_lst.append(item)
        else:
            cnt += 1
            if item[1] == m:
                flag = False
    print(cnt)