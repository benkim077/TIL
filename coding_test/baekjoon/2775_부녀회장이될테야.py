import sys
input = sys.stdin.readline


dp = [[0] * (14 + 1) for _ in range(14 + 1)]
for i in range(15):
    for j in range(1, 15):
        if i == 0:
            dp[i][j] = j
        else:
            dp[i][j] = sum(dp[i - 1][:j + 1])


T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    print(dp[k][n])