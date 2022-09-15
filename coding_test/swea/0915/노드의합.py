# N개의 노드를 갖는 완전 이진 트리
# 리프 노드의 번호와 저장된 값이 주어지면
# 나머지 노드에 자식 노드 값의 합을 저장한 다음,
# 지정한 노드 번호에 저장된 값을 출력하는 프로그램을 작성 하시오.
import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)

    mn = N + 1
    for _ in range(M):
        leaf, value = map(int, input().split())
        mn = min(mn, leaf)
        tree[leaf] = value

    for i in range(mn - 1, 0, -1):
        if i * 2 + 1 < N + 1:
            tree[i] = tree[i * 2] + tree[i * 2 + 1]
        else:
            tree[i] = tree[i * 2]

    print(f'#{tc} {tree[L]}')