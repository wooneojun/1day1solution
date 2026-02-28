import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    for _ in range(M):
        _, _ = map(int, input().split())
    print(N-1)
