from math import floor
import sys
input = sys.stdin.readline


N = int(input())
dp = [0] * (N + 1)

for k in range(1, N + 1):
    root = floor(k ** 0.5)
    mn = 4
    while root > 0:
        temp = k - (root ** 2)
        if dp[temp] > 4:
            break
        mn = min(mn, dp[temp])
        root -= 1

    dp[k] = 1 + dp[mn]

print(dp[N])


# dp = [0] * (50001)
# dp[1] = 1

# for k in range(2, 50001):
#     root = floor(k ** 0.5)
#     mn = 4
#     while root > 0:
#         temp = k - (root ** 2)
#         if dp[temp] > 4:
#             break
#         mn = min(mn, dp[temp])
#         root -= 1

#     dp[k] = 1 + dp[mn]


# N = int(input())

# print(dp[N])