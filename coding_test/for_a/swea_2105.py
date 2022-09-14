'''
시간초과
- 순회 조차도 너무 많은 시간이 걸린다.
- 재귀 호출이 너무 많다? 반복을 이용한 dfs로 풀어볼까
- 가지치기를 더 빡세게?
'''

import sys
sys.stdin = open('input.txt')

di, dj = [-1, 1, 1, -1], [1, 1, -1, -1] # 대각선 방향 델타 탐색

def dfs(m, n, path, k):
    global i, j, cnt

    if k == 3 and m == i and n == j and len(path) >= 3:
        cnt = max(cnt, len(path))
        return

    if 0 <= m < N and 0 <= n < N and data[m][n] not in path:
        new_path = path + [data[m][n]]

        nm, nn = m + di[k], n + dj[k]
        dfs(nm, nn, new_path, k)

        if k < 3:
            nm, nn = m + di[k + 1], n + dj[k + 1]
            dfs(nm, nn, new_path, k + 1)

        
    # if (i, j) == (si, sj) and not is_start:
        # 정답 체크
        # cnt_lst = [0] * 101
        # for m in range(N):
        #     for n in range(N):
        #         if vsted[m][n]:
        #             cnt_lst[data[m][n]] += 1
        # for t in range(1, 101):
        #     if cnt_lst[t] > 1:
        #         pass
        #     else:
        #         temp = sum(cnt_lst)
        #         if mx < temp:
        #             mx = temp
        # return



    # for l in range(2):
    #     k = (k + l) % 4
    #     ni, nj = i + di[k], j + dj[k]
    #     if 0 <= ni < N and 0 <= nj < N and not vsted[ni][nj]:
    #         vsted[ni][nj] = True
    #         bt(ni, nj, k, vsted, False)
    #         vsted[ni][nj] = False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]


    
    cnt = -1
    for i in range(N):
        for j in range(N):
            dfs(i, j, [], 0) # i, j에서 시작, 0은 방향, vsted 방문체크, 시작 지점 여부

    print(cnt)