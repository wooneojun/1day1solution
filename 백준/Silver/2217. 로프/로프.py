n = int(input())
n_list=[]
for _ in range(n):
    n_list.append(int(input()))
n_list.sort()
r_list = []
for i in n_list:
    r_list.append(n * i)
    n -= 1
print(max(r_list))
