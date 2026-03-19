import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
target = '123456780'

def grid_to_len(grid):
    string = ''
    for i in range(3):
        for j in range(3):
            string += grid[i][j]
    return string

def bfs(string):
    visited = set()
    queue = deque([(string, 0)])
    while queue:
        string, var = queue.popleft()
        if target == string:
            return var
        visited.add(string)
        for i in range(4):
            lst = list(string)
            zero_idx = lst.index('0')
            nx = zero_idx//3 +dx[i]
            ny = zero_idx%3 + dy[i]
            dl = 3*nx + ny
            if 0<=nx<3 and 0<=ny<3:
                lst[zero_idx], lst[dl] = lst[dl], lst[zero_idx]
            nstr = "".join(lst)
            if nstr not in visited:
                queue.append([nstr, var+1])
    return -1

grid = [list(input().split())for _ in range(3)]

string = grid_to_len(grid)
print(bfs(string))