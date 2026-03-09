import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

tree = [0] * (N * 4)
arr = [int(input()) for _ in range(N)]

def init(start, end, index):
    if start == end:
        tree[index] = arr[start]
        return tree[index]
    mid = (start + end) // 2
    tree[index] = init(start, mid, index*2) + init(mid+1, end, index*2+1)
    return tree[index]

def interval_sum(start, end, index, left, right):
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return tree[index]
    mid = (start + end) // 2
    return interval_sum(start, mid, index*2, left, right) + interval_sum(mid+1, end, index*2+1, left, right)

def update(start, end, index, what, value):
    if what < start or what > end:
        return
    tree[index] += value
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, index *2, what, value)
    update(mid+1, end, index*2+1, what, value)

init(0, len(arr)-1, 1)

for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        tmp = c - arr[b-1]
        arr[b-1] += tmp
        update(0, len(arr)-1, 1, b-1, tmp)
    elif a == 2:
        print(interval_sum(0, len(arr)-1, 1, b-1, c-1))
