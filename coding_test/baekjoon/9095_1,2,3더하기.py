dp = [0] * (12)
dp[1] = 1
dp[2] = 2
dp[3] = 4
for k in range(4, 12):
    dp[k] = dp[k - 1] + dp[k - 2] + dp[k - 3]


T = int(input())
for _ in range(T):
    N = int(input())
    print(dp[N])