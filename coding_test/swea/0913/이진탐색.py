import sys
sys.stdin = open('input.txt')


def inorder(n):
    global k, N
    if n <= N:
        inorder(n * 2)
        data[n] = k
        k += 1
        inorder(n * 2 + 1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    data = [0] * (N + 1)
    k = 1
    inorder(1)

    print(f'#{tc} {data[1]} {data[N // 2]}')