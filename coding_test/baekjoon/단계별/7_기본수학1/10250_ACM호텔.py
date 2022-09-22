import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T + 1):
    H, W, N = map(int, input().split())

    s, r = divmod(N, H)
    n = s + 1 if r % H else s
    f = r if r % H else r + H

    print(f, end='')
    if n >= 10:
        print(n, end='')
    else:
        print('0', end='')
        print(n, end='')
    print()