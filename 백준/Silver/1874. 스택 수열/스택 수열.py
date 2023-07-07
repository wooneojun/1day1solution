import sys
input = sys.stdin.readline

n = int(input())
s = []
ans = []
flag = True
m = 1

for i in range(n):
    num = int(input())
    while m <= num:
        s.append(m)
        ans.append("+")
        m+=1
    if s[-1] == num:
        s.pop()
        ans.append("-")
    else:
        print("NO")
        flag = False
        break

if flag:
    for i in ans:
        print(i)