import sys
sys.setrecursionlimit(10**6)

def recur(num, lst):
    global N
    if num == int(N**(1/2))+1:
        return lst
    if N%num == 0:
        lst.append(N//num)
        lst.append(num)
    recur(num+1, lst)
        



while True:
    N = int(input())
    if N == -1:
        break
    lst = [1]
    recur(2, lst)
    lst.sort()

    if sum(lst) == N:
        print(f"{N} = ", end="")
        print(" + ".join(map(str, lst)))
    else:
        print(f"{N} is NOT perfect.")
    
    