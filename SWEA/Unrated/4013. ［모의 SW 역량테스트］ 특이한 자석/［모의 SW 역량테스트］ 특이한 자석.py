T = int(input())

def move_gear(gear, dist):
    gear = gear-1
    lst = is_moveable()
    d = -dist
    ptr[gear] +=d
    for i in range(gear, 3):
        if lst[i]:
            d = -d
            ptr[i+1] = ptr[i+1]+d
        else:
            break
    d = -dist
    for j in range(gear-1, -1, -1):
        if lst[j]:
            d = -d
            ptr[j] = ptr[j] + d
        else:
            break
    return
    

def count_point():
    ans =""
    for i in range(3, -1, -1):
        ans += gear_wheels[i][ptr[i]]
    return int(ans, 2)

def is_moveable():
    lst = [0]*3
    if int(gear_wheels[0][(ptr[0]+2)%8]) + int(gear_wheels[1][(ptr[1]-2)%8]) == 1:
        lst[0] = 1
    if int(gear_wheels[1][(ptr[1]+2)%8]) + int(gear_wheels[2][(ptr[2]-2)%8]) == 1:
        lst[1] = 1
    if int(gear_wheels[2][(ptr[2]+2)%8]) + int(gear_wheels[3][(ptr[3]-2)%8]) == 1:
        lst[2] = 1
    return lst

for tc in range(1, 1+T):
    K = int(input())
    gear_wheels = [list(input().split()) for _ in range(4)]
    ptr = [0]*4
    
    for _ in range(K):
        g, dist = map(int, input().split())
        move_gear(g, dist)
    cnt = count_point() 
    print(f"#{tc} {cnt}")
