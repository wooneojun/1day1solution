n_list = list(map(str, input().split('-')))
s_list = []
for i in n_list:
    s_list.append(list(map(int, i.split('+'))))
total = sum(s_list.pop(0))
for j in s_list:
    total -= sum(j)
print(total)
