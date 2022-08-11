import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    lst = list(map(int, input().split()))
    n = len(lst)

    ans = 0
    for i in range(1 << n):
        subs = []
        for j in range(n):
            if i & (1 << j):
                subs += [lst[j]]

                s = 0
                for k in range(len(subs)):
                    s += subs[k]
                if s == 0:
                    ans = 1

    print(f'#{t} {ans}')
