import sys
sys.stdin = open('input.txt')


def bt(lst, k):
    global mx, sm, check

    if lst == sorted_data:
        if (t - k) % 2 == 0:
            if not check:
                sm = get_sum(lst)
                mx = sm
                check = True
            return
        else:
            if not check:
                lst[-1], lst[-2] = lst[-2], lst[-1]
                sm = get_sum(lst)
                mx = sm
                check = True
            return

    # if k >= N:
    #     if t % 2 == 0:
    #         sm = get_sum(lst)
    #         mx = max(mx, sm)
    #         check = True
    #         return
    #     else:
    #         lst[-1], lst[-2] = lst[-2], lst[-1]
    #         sm = get_sum(lst)
    #         mx = max(mx, sm)
    #         check = True
    #         return

    if k == t:
        i = 0
        sm = 0
        while i < N:
            sm += lst[i] * (10 ** (N - 1 - i))
            i += 1
        if not check:
            mx = max(mx, sm)
        return

    for i in range(N - 1):
        for j in range(i + 1, N):
            if lst[i] <= lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
                bt(lst, k + 1)
                lst[i], lst[j] = lst[j], lst[i]


def get_sum(lst):
    i = 0
    sm = 0
    while i < N:
        sm += lst[i] * (10 ** (N - 1 - i))
        i += 1
    return sm


T = int(input())
for tc in range(1, T + 1):
    data, t = input().split()
    data = list(map(int, data))
    t = int(t)

    # max_status 찾기
    sorted_data = sorted(data, reverse=True)

    N = len(data)
    sm = 0
    mx = 0
    check = False
    bt(data, 0)

    print(f'#{tc} {mx}')
