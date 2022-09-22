import sys
sys.stdin = open('input.txt')

def f(i, k, r):
    global mn

    if i == r:
        temp_lst = [1] + p + [1]
        length = len(temp_lst)
        sm = 0
        for i in range(length - 1):
            sm += data[temp_lst[i] - 1][temp_lst[i + 1] - 1]
        mn = min(mn, sm)
    else:
        for j in range(k):
            if not check[j]:
                check[j] = True
                p[i] = lst[j]
                f(i + 1, k, r)
                check[j] = False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    n = N - 1
    r = n
    lst = [i for i in range(2, N + 1)]
    p = [0] * r
    check = [False] * n
    mn = 100 * N
    f(0, n, r)

    print(f'#{tc} {mn}')