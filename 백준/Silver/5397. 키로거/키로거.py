import sys
input = sys.stdin.readline

T_str = input().strip()
if T_str:
    T = int(T_str)
    for _ in range(T):
        word = input().strip()
        left_stack = []
        right_stack = []

        for w in word:
            if w == '<':
                if left_stack:
                    right_stack.append(left_stack.pop())
            elif w == '>':
                if right_stack:
                    left_stack.append(right_stack.pop())
            elif w == '-':
                if left_stack:
                    left_stack.pop()
            else:
                left_stack.append(w)
        
        print("".join(left_stack) + "".join(reversed(right_stack)))