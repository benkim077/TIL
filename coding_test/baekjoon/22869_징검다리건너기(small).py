'''
from collections import deque


def bfs():
    q = deque()
    q.append(0)
    vsted = [False] * N
    vsted[0] = True

    while q:
        i = q.popleft()
        for j in range(i + 1, N):
            if (j - i) * (1 + abs(data[i] - data[j])) <= K and not vsted[j]:
                q.append(j)
                vsted[j] = True
    
    if vsted[N - 1]:
        return True
    else:
        return False


N, K = map(int, input().split())
data = list(map(int, input().split()))

if bfs():
    print('YES')
else:
    print('NO')
'''




# tony
# 시간초과

# N, K = map(int, input().split())
# data = [0] + list(map(int, input().split()))
# dp = [K + 1] * (N + 1)
# dp[1] = 0

# for i in range(1, N):
#     if dp[i] > K:
#         continue

#     for j in range(i + 1, N + 1):
#         temp = (j - i) * (1 + abs(data[i] - data[j]))
#         dp[j] = min(dp[j], temp)

# if dp[N] > K:
#     print('NO')
# else:
#     print('YES')




# 4000ms
# 
# N, K = map(int, input().split())
# data = [0] + list(map(int, input().split()))
# dp = [False] * (N + 1)

# dp[1] = True
# for i in range(1, N):   # 1번 돌부터 N - 1번 돌까지
#     if dp[i]:
#         for j in range(i + 1, N + 1):   # 다음 돌들에 대해서 
#             if (j - i) * (1 + abs(data[i] - data[j])) <= K:     # 이동할 수 있는지 체크
#                 dp[j] = True

# if dp[N]:
#     print('YES')
# else:
#     print('NO')
