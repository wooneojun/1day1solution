
from collections import defaultdict
import heapq
    # 상 하 좌 우
dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]

change_dir = {1:2, 2:1, 3:4, 4:3}
T = int(input())

def move():
    global lst
    dic = defaultdict(list)
    new_lst = []
    for val in lst:
        nr = val[0] + dr[val[3]]
        nc = val[1] + dc[val[3]]
        if nr == 0 or nc == 0 or nr == N-1 or nc==N-1:
            cur_mic = val[2] // 2
            cur_dir = change_dir[val[3]]
        else:
            cur_mic = val[2]
            cur_dir = val[3]
        if cur_mic > 0:
            heapq.heappush(dic[(nr, nc)], (-cur_mic, cur_dir))
    for key, val in dic.items():
        pow, dir = heapq.heappop(val)
        total = -pow
        if len(val) >= 1:
            while val:
                p = heapq.heappop(val)
                total += -p[0]
        new_lst.append([key[0], key[1], total, dir])
    return new_lst

def count():
    global lst
    cnt = 0
    for val in lst:
        cnt += val[2]
    return cnt


for tc in range(1, 1+T):
    N, M, K = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(K)]
    for _ in range(M):
        lst = move()
    print(f"#{tc} {count()}")