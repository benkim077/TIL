import sys

sys.stdin = open('input.txt')


def make_square_arr(lst, M, N):
    if M > N:
        for m in range(M):
            for _ in range(M - N):
                lst[m].append(-1)
    elif M < N:
        for _ in range(N - M):
            lst.append([-1] * N)
    else:
        pass

    return lst


def make_t_arr(lst):
    M = len(lst)
    N = len(lst[0])
    if M != N:
        lst = make_square_arr(lst, M, N)

    length = len(lst)
    for m in range(length):
        for n in range(m + 1, length):
            lst[m][n], lst[n][m] = lst[n][m], lst[m][n]

    return lst


T = int(input())

for tc in range(1, T + 1):
    arr = [list(input()) for _ in range(5)]

    # 길이 최댓값 구하기
    mx = 0
    for i in range(len(arr)):
        if mx < len(arr[i]):
            mx = len(arr[i])
    
    # 길이 보다 짧은 부분을 -1로 채우기
    for i in range(len(arr)):
        if len(arr[i]) < mx:
            for _ in range(mx - len(arr[i])):
                arr[i].append(-1)

    # N * M 행렬을 M * N 전치행렬 만들기
    t_arr = make_t_arr(arr)

    # 출력하기
    print(f'#{tc}', end=' ')
    for i in range(len(t_arr)):
        for j in range(5):
            if t_arr[i][j] != -1:
                print(t_arr[i][j], end='')
    print()

#2 Aa0aPAf985Bz1EhCz2W3D1gkD6x
