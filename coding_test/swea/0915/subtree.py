import sys
sys.stdin = open('input.txt')


def preorder(n):
    global cnt
    if n == 0:
        return

    cnt += 1
    preorder(left[n])
    preorder(right[n])


T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())    # 간선 갯수, 서브트리의 루트
    data = list(map(int, input().split()))

    left, right = [0] * (E + 2), [0] * (E + 2)
    for i in range(E):
        p, c = data[2 * i], data[2 * i + 1]

        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    cnt = 0
    preorder(N)

    print(f'#{tc} {cnt}')