import sys
input = sys.stdin.readline

def init(idx, start, end):
    if start == end:
        segtree[idx] = lst[start]
        return lst[start]
    mid = (start + end)//2
    segtree[idx] = init(idx*2, start, mid) + init(idx*2+1, mid+1, end)
    return segtree[idx]

def add(idx, start, end, first, last):
    if first>end or last<start:
        return 0
    if first<=start and last>=end:
        return segtree[idx]
    mid = (start+end)//2
    return add(idx*2, start, mid, first, last) + add(idx*2+1, mid+1, end, first, last)

def change(idx, start, end, target, value):
    if start>target or end < target:
        return
    segtree[idx] += value
    if start==end:
        return
    mid = (start+end)//2
    change(idx*2, start, mid, target, value)
    change(idx*2+1, mid+1, end, target, value)
    

N, Q = map(int, input().split())
lst = list(map(int, input().split()))
ll = len(lst)
segtree = [0]*(ll*4)
init(1, 0, ll-1)

ans = []
for _ in range(Q):
    x, y, a, b = map(int, input().split())
    if x > y:
        x, y = y, x
    ans.append(add(1, 0, ll-1, x-1, y-1))
    
    change(1, 0, ll-1, a-1, b-lst[a-1])
    lst[a-1]=b

for item in ans:
    print(item)
