import sys, heapq
from collections import defaultdict

input = sys.stdin.readline

suffix_dict = defaultdict(int)

T = int(input())



for _ in range(T):
    min_heap = []
    max_heap = []
    deleted = set()
    N = int(input())
    for _ in range(N):
        oper, num = input().split()
        if oper == "I":
            num = int(num)
            cnt = suffix_dict[num]
            heapq.heappush(min_heap, (num, cnt))
            heapq.heappush(max_heap, (-num, cnt))
            suffix_dict[num] += 1
        else:
            if num == "1":
                while max_heap:
                    n, c = heapq.heappop(max_heap)
                    n = -n
                    if (n, c) in deleted:
                        continue
                    deleted.add((n, c))
                    break
            else:
                while min_heap:
                    n, c = heapq.heappop(min_heap)
                    if (n, c) in deleted:
                        continue
                    deleted.add((n, c))
                    break
    max_tmp, min_tmp = 0, 0
    flag = False
    while max_heap:
        n, c = heapq.heappop(max_heap)
        n = -n
        if (n, c) in deleted:
            continue
        flag = True
        max_tmp = n
        break
    if flag:
        while min_heap:
            n, c = heapq.heappop(min_heap)
            if (n, c) in deleted:
                continue
            min_tmp = n
            break
        print(max_tmp, min_tmp)
    else:
        print("EMPTY")

    