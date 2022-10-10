dp = [[0] * 101 for _ in range(101)]

for n in range(1, 101):
    for m in range(1, 101):
        if m == 1:
            dp[n][m] = n
            continue

        if m > n:
            pass
        elif m == n:
            dp[n][m] = 1
        else:
            dp[n][m] = dp[n - 1][m - 1] + dp[n - 1][m]
            

N, M = map(int, input().split())
print(dp[N][M])