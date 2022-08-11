import sys
sys.stdin = open('../0810/input.txt')

T = int(input())
for t in range(1, T+1):
    (K, N, M) = tuple(map(int, input().split()))
    station = list(map(int, input().split()))

    lst = [0]*(N+1)
    for idx in range(M):
        lst[station[idx]] += 1


    i = 0
    cnt = 0
    while i < N-K:
        s_idx = i
        for j in range(i+K, i, -1):
            if lst[j] == 1:
                i = j
                cnt += 1
                break

        if i == s_idx:
            cnt = 0
            break
    print(f'#{t} {cnt}')