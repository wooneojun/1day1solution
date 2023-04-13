n = int(input())
n_list = []
for _ in range(n):
	n_list.append(list(map(int, input().split())))
n_list.sort()
n_list.sort(key=lambda x: x[1])
end_t = 0
cnt = 0
for i, j in n_list:
	if i >= end_t:
		end_t = j
		cnt += 1
 
print(cnt)