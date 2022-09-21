import sys
sys.stdin = open('input.txt')


def bt(lst, k):
    global mx
    if k == t:
        i = 0
        sm = 0
        while i < N:
            sm += lst[i] * (10 ** (N - 1 - i))
            i += 1
        mx = max(mx, sm)
        return

    for i in range(N - 1):
        for j in range(i + 1, N):
            # if lst[i] < lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
            bt(lst, k + 1)
            lst[i], lst[j] = lst[j], lst[i]


T = int(input())
for tc in range(1, T + 1):
    data, t = input().split()
    data = list(map(int, data))
    t = int(t)

    N = len(data)
    mx = 0
    bt(data, 0)

    print(f'#{tc} {mx}')
