n = int(input())
length = list((map(int, input().split())))
money = list((map(int, input().split())))
small = 1000000000
total = 0
for i in range(len(money)-1):
    if money[i] < small:
        small = money[i]
    total += small * length[i]
print(total)
