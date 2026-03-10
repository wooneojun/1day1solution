import sys
input = sys.stdin.readline

def min_init(start, end, index):
    if start == end:
        min_tree[index] = lst[start]
        return min_tree[index]
    mid = (start+ end) // 2
    min_tree[index] = min(min_init(start, mid, index*2), min_init(mid+1, end, index*2 +1))
    return min_tree[index]

def max_init(start, end, index):
    if start == end:
        max_tree[index] = lst[start]
        return max_tree[index]
    mid = (start+ end) // 2
    max_tree[index] = max(max_init(start, mid, index*2), max_init(mid+1, end, index*2 +1))
    return max_tree[index]

def interval_min(start, end, index, left, right):
    if left>end or right<start:
        return 10**10
    if left<=start and right>=end:
        return min_tree[index]
    mid = (start + end) // 2
    return min(interval_min(start, mid, index*2, left, right), interval_min(mid+1, end, index*2+1, left, right))

def interval_max(start, end, index, left, right):
    if left>end or right<start:
        return 0
    if left<=start and right>=end:
        return max_tree[index]
    mid = (start + end) // 2
    return max(interval_max(start, mid, index*2, left, right), interval_max(mid+1, end, index*2+1, left, right))



N, M = map(int, input().split())
lst = [int(input()) for _ in range(N)]
min_tree = [10**10]*(N*4)
max_tree = [0]*(N*4)

min_init(0, len(lst)-1, 1)
max_init(0, len(lst)-1, 1)
for _ in range(M):
    s, e = map(int, input().split())
    print(f"{interval_min(0, N-1, 1, s-1, e-1)} {interval_max(0, N-1, 1, s-1, e-1)}")