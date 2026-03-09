import sys
input = sys.stdin.readline

K = int(input())
lst = [[] for _ in range(K)]
tree = list(map(int, input().split()))

def recur(v, k):
    if k == 0:
        return
    lst[k-1].append(tree[v])
    recur(v-2**(k-2), k-1)
    recur(v+2**(k-2), k-1)
    

recur(2**(K-1)-1, K)

for i in range(K-1, -1, -1):
    print(*lst[i])
