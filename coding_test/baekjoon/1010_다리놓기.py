import sys
sys.stdin = open('input.txt')


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    dp = [[0] * (N + 1) for _ in range(M + 1)]
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            if j == 1:      # N이 1일 때
                dp[i][j] = i
            elif i == j:    # N, M이 같을 때
                dp[i][j] = 1
            elif i > j:     # 일반적인 경우
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]  # 조합의 점화식
            else:           # N > M인 경우
                pass            # dp[i][j] = 0

    print(dp[M][N])