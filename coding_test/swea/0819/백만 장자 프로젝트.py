import sys


sys.stdin = open('../0818/input.txt')


def get_max_idx(arr):
    mx = 0
    mx_idx = 0
    for i, v in enumerate(arr):
        if mx <= v:
            mx = v
            mx_idx = i

    return mx_idx


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    # lst mx index 구하기
    idx = get_max_idx(lst)

    # mx index까지 계산하기
    sm = 0
    i = 0
    while i < len(lst):
        for j in range(i, i + idx + 1):
            sm += lst[i + idx] - lst[j]
        i += idx + 1
        if i < len(lst):
            idx = get_max_idx(lst[i:])
        else:
            break


    # 출력
    print(f'#{tc} {sm}')

    ''' 시간 초과 코드
    sm = 0
    cnt = 0
    while lst:
        cnt += 1
        sm += lst[idx - cnt + 1] - lst[0]
        lst.pop(0)
        # max index를 넘어가면 다시 최댓값 구하기
        if cnt > idx:
            idx = get_max_idx(lst)
            cnt = 0
    '''
