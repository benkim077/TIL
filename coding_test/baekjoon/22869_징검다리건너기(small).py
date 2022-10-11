N, K = map(int, input().split())
data = [0] + list(map(int, input().split()))
dp = [False] * (N + 1)

dp[1] = True
for i in range(1, N):
    if dp[i] == True:
        for j in range(i + 1, N + 1):
            if (j - i) * (1 + abs(data[i] - data[j])) <= K:
                dp[j] = True

if dp[N]:
    print('YES')
else:
    print('NO')