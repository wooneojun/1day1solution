n = int(input())
lst = []
for i in str(n):
    lst.append(i)
if len(lst) == 1:
    print(n)
elif len(lst) == 2:
    print(9 + 2 * (n-9))
elif len(lst) == 3:
    print(9 + 2 * 90 + 3 *(n-99))
elif len(lst) == 4:
    print(9 + 2 * 90 + 3 * 900 + 4 * (n-999))
elif len(lst) == 5:
    print(9 + 2 * 90 + 3 * 900 + 4 * 9000 + 5 * (n-9999))
elif len(lst) == 6:
    print(9 + 2 * 90 + 3 * 900 + 4 * 9000 + 5 * 90000 + 6 * (n-99999))
elif len(lst) == 7:
    print(9 + 2 * 90 + 3 * 900 + 4 * 9000 + 5 * 90000 + 6 * 900000 + 7 * (n-999999))
elif len(lst) == 8:
    print(9 + 2 * 90 + 3 * 900 + 4 * 9000 + 5 * 90000 + 6 * 900000 + 7 * 9000000 + 8 * (n-9999999))
elif len(lst) == 9:
    print(9 + 2 * 90 + 3 * 900 + 4 * 9000 + 5 * 90000 + 6 * 900000 + 7 * 9000000 + 8 * 90000000 + 9 * (n-99999999))