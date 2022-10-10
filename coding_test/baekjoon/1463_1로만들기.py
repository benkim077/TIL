'''
메모이제이션으로 풀어보려 했는데, 재귀 에러
def solve(k):
    if k == 1:
        return 0
    elif dp[k]:
        return dp[k]
    else:
        if k % 6 == 0:
            dp[k] = min(solve(k // 3), solve(k // 2), solve(k - 1)) + 1
        elif k % 3 == 0:
            dp[k] = min(solve(k // 3), solve(k - 1)) + 1
        elif k % 2 == 0:
            dp[k] = min(solve(k // 2), solve(k - 1)) + 1
        else:
            dp[k] = solve(k - 1) + 1

        return dp[k]


N = int(input())

dp = [0] * (N + 1)

ans = solve(N)
print(ans)'''

'''
tablulation 풀이. (성공)

N = int(input())

dp = [0] * (N + 1)
dp[1] = 0
for k in range(2, N + 1):
    if k % 3 == 0 and k % 2 == 0:
        dp[k] = min(dp[k // 3], dp[k // 2], dp[k - 1]) + 1
    elif k % 3 == 0 and k % 2 != 0:
        dp[k] = min(dp[k // 3], dp[k - 1]) + 1
    elif k % 3 != 0 and k % 2 == 0:
        dp[k] = min(dp[k // 2], dp[k - 1]) + 1
    else:
        dp[k] = dp[k - 1] + 1

print(dp[N])

'''