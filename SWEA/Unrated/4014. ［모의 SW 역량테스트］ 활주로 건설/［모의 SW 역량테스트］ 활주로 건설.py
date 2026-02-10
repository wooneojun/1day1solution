T = int(input())

def find_runway(lst, X):
    global N
    visited = [False] * N
    for i, val in enumerate(lst):
        if val == -1:
            if i+X-1 < N:
                if visited[i]:
                    return 0
                for j in range(X-1):
                    if visited[i]:
                        return 0
                    if j == X-2 and lst[i+j+1] == -1:
                        continue
                    elif lst[i+j+1] != 0:
                        return 0
                visited[i:i+X] = [True]*X
            else:
                return 0
        elif val == 1:
            if i-X >=0:
                for j in range(X):
                    if j == X-1 and lst[i-j-1] == 1:
                        continue
                    elif lst[i-j-1] != 0 or visited[i-j-1]:
                        return 0
                visited[i-X:X] = [True]*X
            else:
                return 0
        elif val > 1 or val < -1:
            return 0
    return 1

def make_prefix(lst):
    new_lst =[0]
    tmp = lst[0]
    for i in range(1, len(lst)):
        new_lst.append(lst[i] - tmp)
        tmp += lst[i] - tmp
    return new_lst
            
        

for tc in range(1, T+1):
    N, X = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for row in grid:
        n_row = make_prefix(row)
        cnt += find_runway(n_row, X)
    for col in range(N):
        n_ol = [grid[i][col] for i in range(N)]
        n_col = make_prefix(n_ol)
        cnt += find_runway(n_col, X)
    print(f"#{tc} {cnt}")
