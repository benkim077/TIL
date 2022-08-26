import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T + 1):
    N, P = map(int, input().split())

    s, r = divmod(N, P)
    lst = [s] * P

    i = 0
    while r > 0:
        lst[i] += 1
        i += 1
        r -= 1

    ans = 1
    for num in lst:
        ans *= num

    print(f'#{tc} {ans}')
