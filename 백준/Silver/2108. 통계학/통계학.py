import sys
input = sys.stdin.readline
num = int(input())

A = [0] * 8002 #0은 인덱스 4000

for i in range(num):
    A[int(input())+4000] += 1

#산술 평균
avg = 0
for i in range(8002):
    if A[i] != 0:
        for j in range(A[i]):
            avg += i - 4000
avg = avg / num
print(round(avg))
#중앙값
cnt = num//2 + 1
mid = 0
for i in range(8002):
    if A[i] != 0:
        for j in range(A[i]):
            cnt -= 1
            if cnt == 0:
                mid = i - 4000
                break
print(mid)
#최빈값, 여러개 있을때 두번째로 작은값 출력
many = max(A)
count = []
for i in range(8002):
    if A[i]== many:
        count.append(i-4000)
if len(count) == 1:
    print(count[0])
else:
    print(count[1])

#범위
div = []
for i in range(8002):
    if A[i]!=0:
        div.append(i)
        break
for i in range(8001,-1,-1):
    if A[i]!=0:
        div.append(i)
        break
print(div[1]-div[0])
