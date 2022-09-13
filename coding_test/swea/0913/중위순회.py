import sys
sys.stdin = open('input.txt')


def inorder(n):
    if n <= N:
        inorder(n * 2)
        print(data[n], end='')
        inorder(n * 2 + 1)


for tc in range(1, 10 + 1):
    N = int(input())
    data = [0] * (N + 1)
    for _ in range(N):
        P, V, *temp = input().split()
        P = int(P)
        data[P] = V

    print(f'#{tc}', end=' ')
    inorder(1)
    print()



