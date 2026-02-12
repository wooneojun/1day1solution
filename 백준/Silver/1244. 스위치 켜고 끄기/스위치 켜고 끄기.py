import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
M = int(input())

for _ in range(M):
    gender, index = map(int, input().split())
    
    if gender == 1:
        num = index - 1
        while num < N:
            if lst[num]:
                lst[num] = 0
            else:
                lst[num] = 1
            num += index
    else:
        num = index - 1
        left = num - 1
        right = num + 1
        if lst[num]:
            lst[num] = 0
        else:
            lst[num] = 1
        flag = False
        while left >= 0 and right < N and not flag:
            if lst[left] == lst[right]:
                if lst[left]:
                    lst[left], lst[right] = 0, 0
                else:
                    lst[left], lst[right] = 1, 1
                left -= 1
                right += 1
            else:
                flag = True
for i in range(len(lst)):
    print(lst[i], end=" ")
    if (i + 1) % 20 == 0:
        print()