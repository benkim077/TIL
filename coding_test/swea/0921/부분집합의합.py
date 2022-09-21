import sys
sys.stdin = open('input.txt')

# N개의 원소를 가지는 부분집합의 합이 K인 부분집합을 찾는 함수
def bt(lst, vsted, prev):
    global N, K, ans

    if len(lst) >= N:
        if sum(lst) == K:
            print(lst)
            ans += 1
        return

    for i in range(1, 12 + 1):
        if not vsted[i] and prev < i:
            vsted[i] = True
            bt(lst + [i], vsted, i)
            vsted[i] = False


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())

    ans = 0
    vsted = [False] * (1 + 12)
    bt([], vsted, 0)

    print(f'#{tc} {ans}')