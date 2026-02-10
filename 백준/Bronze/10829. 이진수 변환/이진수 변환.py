def recur(num):
    if num == 0:
        return
    else:
        recur(num//2)
        print(num%2, end="")
N = int(input())

recur(N)