lst = set(i for i in range(1,10001))
del_lst = set()
for i in range(1,10001):
    del_lst.add(i + i//1000 + i//100%10 + i//10%10 + i %10)
lst = list(lst - del_lst)
lst.sort()

for i in lst:
    print(i)