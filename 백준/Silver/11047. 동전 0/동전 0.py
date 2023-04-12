n, m = map(int, input().split())
num_list = []
cnt = 0

for _ in range(n):
  i = int(input())
  num_list.append(i)
  
num_list.reverse()

for i in num_list:
	cnt += m // i
	m = m % i

print(cnt)