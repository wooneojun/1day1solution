T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    B = N // 4
    target = input()
    st = set()
    num_lst = []

    for i in range(B):
        w = []
        for j in range(N):
            w.append(target[(i+j)%N])
            if len(w) == B:
                st.add("".join(w))
                w.clear()
    for num in st:
        num_lst.append(int(num, 16))
    num_lst.sort()
    print(f"#{tc} {num_lst[-K]}")

                