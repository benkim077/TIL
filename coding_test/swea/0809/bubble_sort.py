import sys
sys.stdin = open('../0810/input.txt')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    for K in range(1, N):
        for i in range(N-K):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]

    print(f'#{t}', end=' ')
    print(*lst)