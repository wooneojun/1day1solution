import sys
input = sys.stdin.readline

str = input().rstrip()
stack = []
length = 0
before = ''

for i in str:
    if i == '(':
        stack.append([length -1, before])
        length = 0
    elif i == ')':
        leng, num = stack.pop()
        length = leng + (int(num) * length)
    else:
        length += 1
        before = i
print(length)