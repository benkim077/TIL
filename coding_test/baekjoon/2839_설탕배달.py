dp = [0] * 5001
dp[3] = 1
dp[5] = 1

for k in range(6, 5001):
    if dp[k - 3] and dp[k - 5]:
        dp[k] = min(dp[k - 3] + 1, dp[k - 5] + 1)
    elif dp[k - 3] and not dp[k - 5]:
        dp[k] = dp[k - 3] + 1
    elif not dp[k - 3] and dp[k - 5]:
        dp[k] = dp[k - 5] + 1
    else:
        dp[k] = 0

N = int(input())

if dp[N] == 0:
    print(-1)
else:
    print(dp[N])