from collections import deque

def bfs(k):
    q = deque()
    q.append((k, 0))

    while q:
        value, cnt = q.popleft()
        if not (0 < value <= 1_000_000):
            continue

        if vsted[value]:
            continue
        vsted[value] = 1

        if value == M:
            break

        q.append((value + 1, cnt + 1))
        q.append((value - 1, cnt + 1))
        q.append((value * 2, cnt + 1))
        q.append((value - 10, cnt + 1))

    return cnt


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    vsted = [0] * 1_000_001
    ans = bfs(N)
    print(f'#{tc} {ans}')