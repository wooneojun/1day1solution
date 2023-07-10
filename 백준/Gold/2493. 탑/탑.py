import sys
input = sys.stdin.readline


n = int(input())
lst = list(map(int, input().split()))
stack = []
num_lst = []
for i in range(n):
    while stack:
        if stack[-1][1] > lst[i]:
            num_lst.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack:
        num_lst.append(0)
    stack.append([i, lst[i]])

print(*num_lst)