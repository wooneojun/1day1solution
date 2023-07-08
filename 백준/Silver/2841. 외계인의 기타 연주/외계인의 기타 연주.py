import sys
input = sys.stdin.readline

N, P = map(int, input().split())
lst = [[] for _ in range(7)]
cnt = 0
for _ in range(N):
    i, j = map(int, input().split())
    if not lst[i]:
        lst[i].append(j)
        cnt += 1
    else:
        while lst[i] and j < lst[i][-1]:
            lst[i].pop()
            cnt += 1
        if not lst[i] or j > lst[i][-1]:
            lst[i].append(j)
            cnt += 1
print(cnt)
    