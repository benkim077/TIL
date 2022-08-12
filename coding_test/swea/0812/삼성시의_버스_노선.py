import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A, B = [0] * N, [0] * N

    for i in range(N):
        A[i], B[i] = tuple(map(int, input().split()))
        # A = [1, 2]
        # B = [3, 5]

    P = int(input())
    lst = [0] * P  # 정류장 지나가는 버스 노선
    C = [int(input()) for _ in range(P)]

    for i in range(N):
        for j in range(A[i] - 1, B[i]):
            lst[j] += 1

    print(f'#{tc}', end=' ')
    for num in C:
        print(lst[num-1], end=' ')
