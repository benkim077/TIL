import sys

sys.stdin = open(r"input.txt","r")


for _ in range(10):
    T = int(input())

    # buffer가 있는 data_list 
    data_list = []
    my_list = []
    for _ in range(100):
        data_list.append([0] + list(map(int, input().split())) + [0])
    data_list.append([0 for _ in range(102)])

    RIGHT = 'right'
    DOWN = 'down'
    LEFT = 'left'

    is_end = False

    # 반복하면서 변하는 임시값
    temp_idx = 0
    temp_value = 0
    for i in range(100):
        i, j = 0, i+1

        # 카운트 변수와 스타트 인덱스
        count = 0
        start_idx = j-1
        
        direction = DOWN
        while not is_end:
            if data_list[i][j] == 1:
                # 방향전환
                # DOWN -> left or right or keep
                if direction == DOWN:
                    if data_list[i][j-1] == 1:
                        direction = LEFT
                    elif data_list[i][j+1] == 1:
                        direction = RIGHT
                    else:
                        pass
                # LEFT -> down or keep
                elif direction == LEFT:
                    if data_list[i+1][j] == 1:
                        direction = DOWN
                    else:
                        pass
                # RIGHT -> down or keep
                elif direction == RIGHT:
                    if data_list[i+1][j] == 1:
                        direction = DOWN
                    else:
                        pass
                # 방향이 Up인 경우는 없음
                else: 
                    pass

                # 이동
                if direction == DOWN:
                    i += 1
                elif direction == RIGHT:
                    count += 1
                    j += 1
                elif direction == LEFT:
                    count += 1
                    j -= 1
                else:
                    pass
            
            # 현재 칸이 0이면 멈추고 다음 라인으로
            elif data_list[i][j] == 0:
                break
            else:
                break
        
        # 최솟값, 인덱스를 저장
        if count > 0:
            if temp_value > count or temp_value == 0:
                temp_idx = start_idx
                temp_value = count

    # 인덱스 출력
    print(f'#{T} {temp_idx}')

'''
#1 18
#2 96
#3 16
#4 5
#5 99
#6 0
#7 97
#8 0
#9 62
#10 3
'''