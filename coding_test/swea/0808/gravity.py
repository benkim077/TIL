import sys
sys.stdin = open('input.txt')


# 오른쪽으로 1번 회전시킨 2차원 배열을 리턴하는 함수
def get_rotate_arr(lst):
    rotated_arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            rotated_arr[j][N - 1 - i] = lst[i][j]
    return rotated_arr


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))

    # 입력값 2차원 배열 넣기
    arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if j < data[i]:
                arr[i][j] = 1
            else:
                arr[i][j] = 0

    # 배열을 회전시키기 (3회전)
    for _ in range(3):
        arr = get_rotate_arr(arr)

    # 회전시킨 배열의 j값을 확인하며 최댓값 구하기
    mx = 0
    for i in range(N):
        cnt = 0
        is_counting = False     # 0을 셀지 말지 결정하는 bool
        for j in range(N):
            if arr[i][j] == 1:                  # 1이 나오면 그때부터 셀 수 있다.
                is_counting = True
            else:
                if is_counting:  # 셀 수 있는 상태에서, 0이 나오면 센다.
                    cnt += 1
        print(i, cnt)
        if mx < cnt:
            mx = cnt

    # 출력
    print(f'#{tc} {mx}')
