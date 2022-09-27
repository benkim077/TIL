import sys
sys.stdin = open('input.txt')


def bt(k, cnt, bat):
    global mn
    if k == N - 1:
        mn = min(mn, cnt)
        return

    if bat == 0:
        return

    if cnt >= mn:
        return


    bt(k + 1, cnt + 1, data[k + 1])     # 다음에 충전 한 경우
    bt(k + 1, cnt, bat - 1)             # 충전 안한 경우


T = int(input())
for tc in range(1, T + 1):
    N, *data = map(int, input().split())
    data = list(data) + [0]

    mn = N - 2  # 최소 충전 횟수
    bt(0, 0, data[0])    # 위치, 교환횟수
    print(f'#{tc} {mn}')