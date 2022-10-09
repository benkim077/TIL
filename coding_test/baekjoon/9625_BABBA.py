dp = [[0, 0] for _ in range(46)]
dp[0][0], dp[0][1] = 1, 0

for k in range(1, 46):
    dp[k][0] = dp[k - 1][1]
    dp[k][1] = dp[k - 1][0] + dp[k - 1][1]


K = int(input())
print(*dp[K])