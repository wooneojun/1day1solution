import sys
input = sys.stdin.readline

def make_bin(num):
    tmp = bin(num)[2:]
    return tmp.zfill(max_length)

def insert(num):
    binary = make_bin(num)

    now = trie
    for b in binary:
        now = now.setdefault(int(b), dict())
def compare(num):
    now = trie
    binary = make_bin(num)
    res = ""
    for b in binary:
        check = 1-int(b)
        if check in now:
            res += "1"
            now = now[check]
        else:
            res += "0"
            now = now[1-check]
    return int(res, 2)
trie = dict()

N = int(input())
lst = list(map(int, input().split()))
max_length = len(bin(max(lst)))-2

for num in lst:
    insert(num)
max_num = 0
for num in lst:
    max_num = max(max_num, compare(num))
print(max_num)