import sys
sys.stdin = open('input.txt')

def postorder(n):
    if n == 0:
        return

    postorder(left[n])
    postorder(right[n])
    if tree[n] == '-':
        tree[n] = tree[left[n]] - tree[right[n]]
    elif tree[n] == '+':
        tree[n] = tree[left[n]] + tree[right[n]]
    elif tree[n] == '*':
        tree[n] = tree[left[n]] * tree[right[n]]
    elif tree[n] == '/':
        tree[n] = tree[left[n]] / tree[right[n]]


T = 10
for tc in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)
    left, right = [0] * (N + 1), [0] * (N + 1)


    for _ in range(N):
        data = list(input().split())
        if not data[1].isnumeric():
            tree[int(data[0])] = data[1]
            left[int(data[0])], right[int(data[0])] = int(data[2]), int(data[3])
        else:
            tree[int(data[0])] = int(data[1])

    postorder(1)
    ans = int(tree[1])
    print(f'#{tc} {ans}')