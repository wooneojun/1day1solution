C, R = map(int, input().split())
K = int(input())

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
grid = [[0]*C for _ in range(R)]
row, col = 0, 0
dir = 0
if C*R<K:
    print(0)
else:
    for s in range(1, C*R+1):
        if s == K:
            print(col+1, row+1)
            break
        else:
            grid[row][col] = s
            row += dx[dir]
            col += dy[dir]
            if row<0 or col<0 or row>=R or col>=C or grid[row][col]:
                row-= dx[dir]
                col -= dy[dir]
                dir = (dir+1) % 4
                row += dx[dir]
                col += dy[dir]