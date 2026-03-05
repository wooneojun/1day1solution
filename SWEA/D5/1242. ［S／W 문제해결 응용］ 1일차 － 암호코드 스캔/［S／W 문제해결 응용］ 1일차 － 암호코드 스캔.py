T = int(input())

opened_code = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4
               , '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011':9}

def decode(lst):
    tmp = []
    for i in range(0, 8):
        tmp.append(opened_code[lst[i*7:i*7+7]])
    num = 0
    for i in range(0, 8, 2):
        num += tmp[i] *3
        num += tmp[i+1]
    if num%10:
        return 0
    else:
        return sum(tmp)


for tc in range(1, T+1):
    N, M = map(int, input().split())

    grid = [input().strip() for _ in range(N)]
    # 이전의 암호를 세트로 저장
    code = set()
    ans = 0

    for i in range(N):
        # 전부 '0'이 아닌 경우 암호 확인
        if len(set(grid[i])) >= 2:
            string = ""
            g = grid[i]

            # 16진수 to 2진수
            for s in g:
                b = bin(int(s, 16))[2:]
                string += '0'*(4-len(b))+b

            # 맨 뒤에서 시작해서 탐색
            idx = len(string) - 1
            while idx >= 55:
                if string[idx] == '1':
                    tmp_multiple = 1


                    while idx - 55 * tmp_multiple >= 0:
                        # 한 번에 전체 56자리를 뽑아 확인
                        nstring = string[idx - 55*tmp_multiple : idx+1 : tmp_multiple]

                        is_valid = True
                        for k in range(8):
                            if nstring[k*7 : k*7+7] not in opened_code:
                                is_valid = False
                                break

                        # 8개가 다 정상일 때만 정상 암호로 인정
                        if is_valid:
                            break
                        tmp_multiple += 1

                    if nstring not in code:
                        code.add(nstring)
                        ans += decode(nstring)
                    # 암호 길이만큼 점프
                    idx -= 56 * tmp_multiple
                else:
                    idx -= 1

    print(f"#{tc} {ans}")