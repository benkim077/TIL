import sys

sys.stdin = open('input.txt')

lst = [2, 3, 5, 7, 11]

T = int(input())

for tc in range(1, T+1):
    cnt = [0, 0, 0, 0, 0] # a, b, c, d, e

    N = int(input())

    for i in range(len(lst)):
        while True:
            if N % lst[i] == 0:
                N = N // lst[i]
                cnt[i] += 1
            else:
                break

    print(f'#{tc}', end=' ')
    for j in range(len(cnt)):
        print(f'{cnt[j]}', end=' ')
    print()
