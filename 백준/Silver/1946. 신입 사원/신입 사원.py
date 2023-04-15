import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    m = int(input())
    man = []
    for _ in range(m):
        man.append(list(map(int, input().split())))
    man.sort()
    atleast = man[0][1]
    cnt = m
    for i in range(1, m):
        if man[i][1] > atleast:
            cnt -= 1
        else:
            atleast = man[i][1]
    print(cnt)