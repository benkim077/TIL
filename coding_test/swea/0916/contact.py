# 그래프를 만들어서 bfs하고 마지막 방문 데이터 중 가장 큰 숫자를 리턴
from collections import deque
import sys
sys.stdin = open('input.txt')


def bfs(n):
    q = deque()
    vsted[n] += 1
    q.append(n)

    while q:
        v = q.popleft()
        for w in range(1, len(link_arr[v])):
            if link_arr[v][w] and not vsted[w]:
                q.append(w)
                vsted[w] = vsted[v] + 1

    return vsted[v]


T = 10
for tc in range(1, T + 1):
    N, target = map(int, input().split())
    data = list(map(int, input().split()))

    link_arr = [[False] * 101 for _ in range(101)]
    for i in range(N):
        if i % 2 == 0:
            link_arr[data[i]][data[i + 1]] = True
    
    
    vsted = [0] * 101
    mx_value = bfs(target)


    # print(vsted)
    ans = 0
    for i in range(101):
        if vsted[i] == mx_value:
            ans = max(ans, i)

    print(f'#{tc} {ans}')

    