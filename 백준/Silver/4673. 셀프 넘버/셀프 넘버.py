nat_num = set(range(1,10000))
del_num = set()

for i in range(1,10000):
    for j in str(i):
        i += int(j)
    del_num.add(i)
self_num = sorted(nat_num - del_num)

for i in self_num:
    print(i)