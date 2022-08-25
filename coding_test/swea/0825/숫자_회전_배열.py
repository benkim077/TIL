'''
N x N 행렬이 주어질 때,
시계 방향으로 90도, 180도, 270도 회전한 모양을 출력하라.
'''
import sys
sys.stdin = open('input.txt')


# N*N 2차원 배열을 입력받아 오른쪽으로 90도 회전한 배열을 출력하는 함수
def turn_arr(arr):
    global N
    t_arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            t_arr[i][j] = arr[N - j - 1][i]
    return t_arr


T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    data = [list(map(int, input().split())) for _ in range(N)]

    data1 = turn_arr(data)
    data2 = turn_arr(data1)
    data3 = turn_arr(data2)

    print(f'#{tc}')
    for i in range(N):
        print(''.join(map(str, data1[i])), ''.join(map(str, data2[i])), ''.join(map(str, data3[i])))