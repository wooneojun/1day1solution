lst = list(input())
final = 0
ki = 1
stack = []

for i in range(len(lst)):
    if lst[i] == '(':
        ki *= 2
        stack.append(lst[i])
    elif lst[i] == '[':
        ki *= 3
        stack.append(lst[i])
    elif lst[i] == ')':
        if not stack or stack[-1] !='(':
            final = 0
            break
        if lst[i-1] == '(':
            final += ki
        ki = ki // 2
        stack.pop()
    elif lst[i] == ']':
        if not stack or stack[-1] != '[':
            final = 0
            break
        if lst[i-1] == '[':
            final += ki
        ki = ki // 3
        stack.pop()

if len(stack) == 0:
    print(final)
else:
    print(0)