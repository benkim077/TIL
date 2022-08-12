import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, Q = tuple(map(int, input().split()))

    lst = [0] * N
    for i in range(Q):
        L, R = tuple(map(int, input().split()))

        for j in range(L-1, R):
            lst[j] = i + 1

    print(f'#{tc}', end=' ')
    for k in range(N):
        print(lst[k], end=' ')