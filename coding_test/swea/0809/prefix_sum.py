import sys
sys.stdin = open('../0810/input.txt')

T = int(input())
for t in range(1, T+1):
    N, M = tuple(map(int, input().split()))
    lst = list(map(int, input().split()))

    mn = M*10000
    mx = M*1

    for i in range(0, N-M+1):
        temp = 0
        for j in range(i, i+M):
            temp += lst[j]
        if mn > temp:
            mn = temp
        if mx < temp:
            mx = temp
    print(f'#{t} {mx-mn}')