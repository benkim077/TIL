from itertools import combinations
import sys
sys.stdin = open('input.txt')


def check_data(arr):
    t_arr = list(zip(*arr))
    # print(t_arr)
    
    for i in range(W):
        for j in range(0, D - K + 1):
            # print(t_arr[i][j: j + K])
            temp = sum(t_arr[i][j: j + K])
            if temp == 0 or temp == K:
                break
        else:
            return False
        # print('---')
    return True



T = int(input())
for tc in range(1, T + 1):
    D, W, K = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(D)]

    # 바로 성능검사 통과하는 경우
    if check_data(data):
        ans = 0
    
    # if ans != 0:


    # print(f'#{tc} {ans}')



    # d개 바꿨을 때 통과