import sys
sys.stdin = open('input.txt')


def preorder(n):
    if n:
        ans_lst.append(n)
        preorder(left[n])
        preorder(right[n])


T = int(input())
for tc in range(1, T + 1):
    V = int(input())
    data = list(map(int, input().split()))

    left, right = [0] * (V + 1), [0] * (V + 1)
    for i in range(V - 1):
        p, c = data[2 * i], data[2 * i + 1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    ans_lst = []
    preorder(1)

    print(f'#{tc}', end=' ')
    print(*ans_lst)
