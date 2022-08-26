import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())     # N 사람 수, M초에 K개 만든다.
    data = list(map(int, input().split()))  # 도착하는 시간
    max_time = max(data)

    # 도착하는 시간의 최댓값 만큼 루프를 돌린다.
    bread = 0
    ans = 'Possible'
    for sec in range(1, max_time + 1):
        if sec % M == 0:
            bread += K

        if sec in data:
            bread -= 1

        if bread < 0:
            ans = 'Impossible'
            break

    # 0초에 도착하는 사람이 있는 경우는 불가능
    if 0 in data:
        ans = 'Impossible'

    print(f'#{tc} {ans}')