a = list(input())
turn = 0
for i in range(len(a)-1):
    if a[i] != a[i+1]:
        turn += 1
print(turn//2 + turn%2)