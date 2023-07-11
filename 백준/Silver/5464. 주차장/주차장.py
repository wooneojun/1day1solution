from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
money = deque()
weight = deque()
wait = deque()
use = [0] * n

cnt = 0

for _ in range(n):
    money.append(int(input()))
for _ in range(m):
    weight.append(int(input()))

for _ in range(2*m):
    car = int(input())
    if car > 0:
        if 0 in use:
            for j in range(n):
                if use[j] == 0:
                    use[j] = car
                    break
        else:
            wait.append(car)
    else:
        a = use.index(-car)
        use[a] = 0
        cnt += weight[-car -1] * money[a]
        if wait:
            use[a] = wait.popleft()
print(cnt)