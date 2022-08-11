import sys

sys.stdin = open('0810/input.txt')

T = int(input())

for t in range(1,T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    mn = mx = lst[0]
    for i in range(1, N):
        if mn > lst[i]:
            mn = lst[i]
        if mx < lst[i]:
            mx = lst[i]
    
    print(f'#{t} {mx-mn}')
