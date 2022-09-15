import sys
sys.stdin = open('input.txt')


def change(pointer):
    if pointer == 1:
        return

    p = pointer // 2    # parent
    if tree[p] > tree[pointer]:
        tree[p], tree[pointer] = tree[pointer], tree[p]
        change(p)
    else:
        return


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))

    tree = [0] * (N + 1)
    pointer = 1
    # 최소힙 만들기
    for ele in data:
        tree[pointer] = ele
        change(pointer)
        pointer += 1

    # 마지막 노드의 조상 노드의 합 구하기
    pointer -= 1
    ans = 0
    while pointer > 1:
        pointer = pointer // 2
        ans += tree[pointer]

    print(f'#{tc} {ans}')
