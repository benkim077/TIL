import sys
sys.stdin = open('input.txt')


def bt(i, j, ans, k):
    if k >= 6:
        ans_lst.append(ans)
        return

    for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        ni, nj = i + di, j + dj
        if 0 <= ni < 4 and 0 <= nj < 4:
            bt(ni, nj, ans + str(data[ni][nj]), k + 1)



T = int(input())
for tc in range(1, T + 1):
    data = [list(map(int, input().split())) for _ in range(4)]
    # print(data)

    ans_lst = []
    for si in range(4):
        for sj in range(4):
            bt(si, sj, str(data[si][sj]), 0)    # 위치, 수, 몇 번째

    # print(ans_lst)
    print(f'#{tc} {len(set(ans_lst))}')
