import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    a = int(input())
    lst = list(map(int, input().split()))
    lst.reverse()
    max = lst[0]
    res = 0

    for i in range(1, len(lst)):
        if max < lst[i]:
            max = lst[i]
            continue
        res += max - lst[i]

    print(res)