'''
#1 1
#2 4
#3 27
#4 11
#5 42
#6 32
#7 2
#8 3
'''
import sys
sys.stdin = open('input.txt')




def bt(k, sm):
    global mn

    if sm >= B:
        mn = min(mn, sm)
        return

    if k == N:
        if sm >= B:
            mn = min(mn, sm)
        return

    bt(k + 1, sm)
    bt(k + 1, sm + data[k])

T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())    # 점원 수, 선반 높이
    data = list(map(int, input().split()))

    vsted = [False] * N
    mn = 10_000 * N
    bt(0, 0)  # 0번째, sm

    ans = mn - B
    print(f'#{tc} {ans}')
