# import sys
# sys.stdin = open('input.txt')

def bt(k, s):   # k 직원의 일을 선택하는 함수, 지금까지 곱한 값 s
    global ans

    if s <= ans:
        return

    if k == N + 1:
        ans = max(ans, s)
        return

    for j in range(1, N + 1):
        if not vsted[j]:
            vsted[j] = True
            bt(k + 1, s * P[k][j] * 0.01)
            vsted[j] = False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    P = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

    ans = 0
    vsted = [0] * (N + 1)
    bt(1, 1)
    print(f'#{tc} {ans * 100:.6f}')