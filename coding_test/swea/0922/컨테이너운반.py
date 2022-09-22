import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    w_data = sorted(list(map(int, input().split())), reverse=True)    # 화물의 무게
    t_data = sorted(list(map(int, input().split())), reverse=True)    # 트럭의 용량

    ans = 0
    n = 0
    for m in range(M):
        while n < N:
            if w_data[n] <= t_data[m]:
                ans += w_data[n]
                n += 1
                break
            else:
                n += 1

    print(f'#{tc} {ans}')