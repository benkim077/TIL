dp = [0] * (1001)
dp[1] = True    # SK
dp[2] = False   # CY
dp[3] = True    # SK
for k in range(4, 1001):
    dp[k] = not(dp[k - 3]) or not(dp[k - 1])

N = int(input())
if dp[N]:
    print('SK')
else:
    print('CY')