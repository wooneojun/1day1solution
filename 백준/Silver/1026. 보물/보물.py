n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)
total = 0
for a, b in zip(A, B):
    total += a * b
print(total)
