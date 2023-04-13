n = int(input())
total = 0
cnt = 0
for i in range(1, n + 1):
    total += i
    if total <= n:
        cnt += 1
    else:
        break
print(cnt)
