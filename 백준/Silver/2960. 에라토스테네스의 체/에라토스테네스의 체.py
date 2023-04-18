import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = [i for i in range(2, N + 1)]
cnt = 0
flag = 2
while True:
    fst = lst.pop(0)
    flag = fst
    cnt += 1
    if cnt == K:
        break
    for i in lst:
        if i % fst == 0:
            cnt += 1
            flag = i
            lst.remove(i)
            if cnt == K:
                break
    if cnt == K:
        break
print(flag)