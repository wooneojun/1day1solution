a = list(input())
a.sort()
b = list(set(a))
b.sort()
c = []

for i in b:
    c.append(a.count(i))
cnt = 0
mid = ""
for i in c:
    if i % 2 == 1:
        cnt += 1
        mid += b[c.index(i)]

if cnt>1:
    print("I'm Sorry Hansoo")
else:
    res = ""
    for i in b:
        res += i * (c[b.index(i)]//2)
    print(res + mid + res[::-1])