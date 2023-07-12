import sys
input = sys.stdin.readline

n, k = map(int, input().split())
student = [0] * n
num = [0] * 21
count = 0

for i in range(n):
    student[i] = len(input().strip())
    if i > k:
        num[student[i - k - 1]] -= 1
    count += num[student[i]]
    num[student[i]] += 1

print(count)