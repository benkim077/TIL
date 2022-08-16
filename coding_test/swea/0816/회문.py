import sys

sys.stdin = open('input.txt')


def is_palindrome(st):
    for k in range(len(st) // 2):
        if st[k] == st[- 1 - k]:
            pass
        else:
            return False
    return True


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr_data = [list(input()) for _ in range(N)]

    ans = 0
    is_found = 0
    # 가로 방향 확인
    for i in range(N):
        for j in range(N - M + 1):
            is_found = is_palindrome(arr_data[i][j: j + M])
            if is_found:
                ans = arr_data[i][j: j + M]
                break
        if is_found:
            break
    if is_found:
        ans = ''.join(ans)
        print(f'#{tc} {ans}')
        continue

    # 전치행렬 만들기
    for i in range(N):
        for j in range(i + 1, N):
            arr_data[i][j], arr_data[j][i] = arr_data[j][i], arr_data[i][j]

    # 세로 방향 확인
    for i in range(N):
        for j in range(N - M + 1):
            is_found = is_palindrome(arr_data[i][j: j + M])
            if is_found:
                ans = arr_data[i][j: j + M]
                break
        if is_found:
            break
    if is_found:
        ans = ''.join(ans)
        print(f'#{tc} {ans}')
        continue
