import sys
sys.stdin = open('input.txt')

def bt(k, sm):  # k번째 행을 선택하는 함수
    global ans

    if k == N + 1:
        ans = max(ans, sm)
        return

    for j in range(1, N + 1):
        if not vsted[j]:
            vsted[j] = True
            bt(k + 1, sm * P[k][j] * 0.01)
            vsted[j] = False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    P = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

    ans = 0
    vsted = [0] * (N + 1)   # 몇 번째 열이 선택 여부 확인 배열
    max_lst = [0] * (N + 1)
    bt(1, 1)
    print(f'#{tc} {ans * 100}')