import sys
sys.stdin = open('input.txt')

T = 10

for t in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    idx_mn = 0
    idx_mx = 0

    # N 번 덤프 돌리기
    for _ in range(N):
        # 최소, 최대 idx 찾기
        for i in range(1, 100):
            if lst[idx_mn] > lst[i]:
                idx_mn = i
            if lst[idx_mx] < lst[i]:
                idx_mx = i
        # 최소와 최대가 같아졌다면, 그만
        if lst[idx_mx] - lst[idx_mn] <= 1:
            break
        else:
            # 덤프 처리 (최소 + 1, 최대 -1)
            lst[idx_mn] += 1
            lst[idx_mx] -= 1
    # 출력하기
    ans = lst[idx_mx] - lst[idx_mn]
    print(f'#{t} {ans}')
