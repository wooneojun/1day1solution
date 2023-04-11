sugar = int(input())
three = 0
five = 0
check = 0

five = sugar // 5

while five >= 0:
    if (sugar - (five * 5)) % 3 == 0:
        three = (sugar - (five * 5)) // 3
        check = five + three
        print(check)
        break
    else:
        five -= 1
if check == 0:
    print(-1)