import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())    # 점원 수, 선반 높이
    data = list(map(int, input().split()))

    for i in range(1 << N):
        for j in range(N):
            print(i & (2 ** j))