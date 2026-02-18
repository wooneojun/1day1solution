def move_gear(gear_num, dist):
    gear_idx = gear_num - 1
    move_list = is_moveable()
    
    # 각 톱니가 어느 방향으로 돌지 미리 계산 (0이면 안 돎)
    directions = [0] * 4
    directions[gear_idx] = dist
    
    # 오른쪽 방향 전파
    for i in range(gear_idx, 3):
        if move_list[i]:
            directions[i+1] = -directions[i]
        else:
            break
            
    # 왼쪽 방향 전파
    for i in range(gear_idx, 0, -1):
        if move_list[i-1]:
            directions[i-1] = -directions[i]
        else:
            break
            
    # 확정된 방향으로 포인터 이동
    for i in range(4):
        if directions[i] != 0:
            # 시계 방향(1)이면 인덱스 -1, 반시계(-1)면 인덱스 +1
            ptr[i] = (ptr[i] - directions[i]) % 8
    
def count_point():
    score = 0
    # 백준 방식: 1번(1점), 2번(2점), 3번(4점), 4번(8점)
    for i in range(4):
        if gear_wheels[i][ptr[i]] == '1': # S극인 경우
            score += (2 ** i)
    return score

def is_moveable():
    lst = [0] * 3
    # 톱니끼리 맞물리는 지점: 왼쪽 톱니의 2번(3시), 오른쪽 톱니의 6번(9시)
    for i in range(3):
        # 현재 포인터를 기준으로 상대적 위치 계산
        left_side = gear_wheels[i][(ptr[i] + 2) % 8]
        right_side = gear_wheels[i+1][(ptr[i+1] + 6) % 8]
        if left_side != right_side:
            lst[i] = 1
    return lst



gear_wheels = [input().strip() for _ in range(4)]
K = int(input())
ptr = [0]*4

for _ in range(K):
    g, dist = map(int, input().split())
    move_gear(g, dist)
cnt = count_point()
print(f"{cnt}")
