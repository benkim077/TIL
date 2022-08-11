import sys
sys.stdin = open('../0810/input.txt')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    lst = list(map(int, input()))

    cnt = [0]*10
    for i in range(N):
        cnt[lst[i]] += 1

    max = 0
    idx = -1
    for i in range(10):
        if max <= cnt[i]:
            max = cnt[i]
            idx = i

    print(f'#{t} {idx} {max}')