# '가능'한 모든 경우
    # n은 행 번호
    # 트리를 만들 때 일반화해서 적어야 한다.

import sys
sys.stdin = open('input.txt')


def dfs(n, sm):
    global ans, vsted
    # 가지 치기
    if ans <= sm:
        return

    # 종료 조건
    if n >= N:
        if ans > sm:
            ans = sm
        return

    # 하부 함수 호출
    for j in range(N):
        if not vsted[j]:
            vsted[j] = True
            dfs(n + 1, sm + data[n][j])
            vsted[j] = False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    vsted = [False] * N
    ans = 10 * N

    dfs(0, 0)

    print(f'#{tc} {ans}')
