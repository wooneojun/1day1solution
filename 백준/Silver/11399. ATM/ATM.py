n = int(input())
num_list = list(map(int, input().split()))
num_list.sort()
total = 0
time = 0
for i in num_list:
    time += i
    total += time
print(total)