import sys
input = sys.stdin.readline

grid = [list(map(int, input().split())) for _ in range(9)]
zero_pos = []

row_check = [[False] * 10 for _ in range(9)]
col_check = [[False] * 10 for _ in range(9)]
box_check = [[False] * 10 for _ in range(9)]

def get_box_num(x, y):
    return (x // 3) * 3 + (y // 3)

for i in range(9):
    for j in range(9):
        if grid[i][j] == 0:
            zero_pos.append((i, j))
        else:
            num = grid[i][j]
            box_num = get_box_num(i, j)
            row_check[i][num] = True
            col_check[j][num] = True
            box_check[box_num][num] = True

length = len(zero_pos)

def dfs(depth):
    if depth == length:
        for i in range(9):
            print(*grid[i])
        return True
        
    x, y = zero_pos[depth]
    box_num = get_box_num(x, y)
    
    for num in range(1, 10):
        if not row_check[x][num] and not col_check[y][num] and not box_check[box_num][num]:
            row_check[x][num] = col_check[y][num] = box_check[box_num][num] = True
            grid[x][y] = num
            
            if dfs(depth + 1):
                return True
            
            row_check[x][num] = col_check[y][num] = box_check[box_num][num] = False
            grid[x][y] = 0
    return False

dfs(0)