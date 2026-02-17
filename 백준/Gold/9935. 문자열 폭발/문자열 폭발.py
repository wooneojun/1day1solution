text = input()
pattern = input()

stack = []
pattern_length = len(pattern)
last_char = pattern[-1] # 패턴의 마지막 글자

for char in text:
    stack.append(char)
    
    # 현재 문자가 패턴의 마지막 글자와 같을 때만 검사
    if char == last_char and len(stack) >= pattern_length:
        # 스택의 뒷부분이 패턴과 일치하는지 확인
        if "".join(stack[-pattern_length:]) == pattern:
            # 일치하면 패턴 길이만큼 스택에서 제거
            for _ in range(pattern_length):
                stack.pop()

result = "".join(stack)
if result:
    print(result)
else:
    print("FRULA")