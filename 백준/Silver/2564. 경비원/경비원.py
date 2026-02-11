X, Y = map(int, input().split())
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.append(list(map(int, input().split())))
Total_leng = 2*X+2*Y
obs_leng = []
for pos, dis in lst:
    if pos == 1:
        obs_leng.append(X-dis)
    elif pos == 3:
        obs_leng.append(X+dis)
    elif pos == 2:
        obs_leng.append(X+Y+dis)
    elif pos == 4:
        obs_leng.append(Total_leng-dis)

cnt = 0
for i in range(len(obs_leng)-1):
    num = abs(obs_leng[-1]-obs_leng[i])
    cnt += min(num, Total_leng-num)
print(cnt)