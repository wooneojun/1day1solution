import sys
input = sys.stdin.readline

N, M = map(int, input().split())
string= []
for i in range(M):
    string.append(list(map(int, input().split())))
one = sorted(string, key=lambda x: x[1])
string.sort()
if one[0][1] * 6 < string[0][0]:
    string[0][0] = one[0][1] * 6
if one[0][1] * (N % 6) > string[0][0]:
    print(string[0][0] * (N // 6 + 1))
else:
    print(string[0][0] * (N // 6) + one[0][1] * (N % 6))