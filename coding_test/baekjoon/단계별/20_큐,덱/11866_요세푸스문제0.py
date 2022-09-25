from collections import deque

N, K = map(int, input().split())

ans = []
q = deque([i for i in range(1, N + 1)])
while q:
    q.rotate(-(K - 1))
    ans.append(q.popleft())

print('<', end='')
for i in range(N):
    print(ans[i], end='')
    if i == N - 1:
        pass
    else:
        print(',', end=' ')
print('>')
