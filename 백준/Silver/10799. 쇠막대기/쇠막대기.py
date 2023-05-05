lst = list(input())
res = 0
stc = []

for i in range(len(lst)):
    if lst[i] == '(':
        stc.append('(')
    else:
        if lst[i-1] == '(':
            stc.pop()
            res += len(stc)
        else:
            stc.pop()
            res += 1
print(res)