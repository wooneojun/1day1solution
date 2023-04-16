n, m = map(int, input().split())
lst = list(range(1, n+1))

die_lst = []
index = 0

for i in range(n):
    index = (index + m - 1) % len(lst)
    die_lst.append(lst.pop(index))
print("<", ", ".join(map(str, die_lst)), ">", sep="")