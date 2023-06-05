import sys
input = sys.stdin.readline

A, B = map(int, input().split())
flag = 1
while(True):
    if B == A:
        break
    elif B % 10 == 1:
        B = B // 10
    else:
        B = B / 2
    flag += 1
    if B < A or B - int(B) != 0:
        flag = -1
        break
print(flag)