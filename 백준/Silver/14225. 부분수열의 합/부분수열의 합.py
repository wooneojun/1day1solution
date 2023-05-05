import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
answer = []

def dfs(value, index):
    if index == n:
        return
    value += arr[index]
    answer.append(value)
    dfs(value, index+1)
    value -= arr[index]
    dfs(value, index+1)

dfs(0,0)
a = set(answer)
for num in range(1, 2000000):
    if num not in a:
        print(num)
        break