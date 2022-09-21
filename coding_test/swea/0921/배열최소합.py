import sys
sys.stdin = open('input.txt')


def bt(lst, k, sm):
    global mn

    if len(lst) == N:
        mn = min(mn, sm)
        return

    if sm >= mn:
        return

    for i in range(N):
        if not vsted[i]:
            vsted[i] = True
            bt(lst + [i], k + 1, sm + data[k][i])
            vsted[i] = False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]

    # 0 ~ N - 1 중에서 N개를 선택 (순서가 상관 있음)
    mn = 10 * N
    vsted = [False] * N
    bt([], 0, 0)

    print(f'#{tc} {mn}')