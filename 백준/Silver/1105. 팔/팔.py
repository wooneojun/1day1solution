a, b = map(str, input().split())
a = list(a)
b = list(b)
res = 0
if len(a)!=len(b):
    res = 0
else:
    for i in range(len(a)):
        if a[i] == b[i]:
            if a[i] == '8':
                res+=1
        else:
            break
print(res)