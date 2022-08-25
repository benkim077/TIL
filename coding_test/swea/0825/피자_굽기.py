import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    data = [0] + list(map(int, input().split()))

    q = []

    for i in range(N):
        q.append((i + 1, data[i + 1]))
    i += 1

    while q:
        ans, cheese = q.pop(0)
        cheese //= 2

        if cheese == 0:
            if i < M:
                q.append((i + 1, data[i + 1]))
                i += 1
        else:
            q.append((ans, cheese))

    print(f'#{tc} {ans}')