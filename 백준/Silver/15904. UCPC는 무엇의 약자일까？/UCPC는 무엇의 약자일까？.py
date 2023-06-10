import sys
input = sys.stdin.readline
lst = ['U', 'C', 'P', 'C']
ucpc = input()
res = True
for i in lst:
    if i in ucpc:
        ucpc = ucpc[ucpc.find(i)+1:]
    else:
        res = False

if res:
    print("I love UCPC")
else:
    print("I hate UCPC")