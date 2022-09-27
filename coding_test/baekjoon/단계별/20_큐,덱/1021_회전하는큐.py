from collections import deque


N, M = map(int, input().split())
data_lst = list(map(int, input().split()))

cnt = 0
dq = deque([i for i in range(1, N + 1)])
for num in data_lst:
    if dq[0] == num:
        dq.popleft()
    else:
        idx = dq.index(num)
        if idx <= len(dq)//2:
            dq.rotate(-(idx))
            cnt += idx
        else:
            dq.rotate(len(dq) - idx)
            cnt += len(dq) - idx
        dq.popleft()

print(cnt)