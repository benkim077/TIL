import sys
sys.stdin = open('input.txt')


def bt(k, sm):
    global mn

    if k == N:
        mn = min(mn, sm)
        return

    if sm >= mn:
        return

    for i in range(N):
        if not vsted[i]:
            vsted[i] = True
            bt(k + 1, sm + data[i][k])
            vsted[i] = False

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    mn = 100 * N
    vsted = [False] * N
    bt(0, 0)    # 0번째 제품 선택, 합은 0

    print(f'#{tc} {mn}')