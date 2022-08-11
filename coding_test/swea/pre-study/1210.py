for _ in range(10):
    T = int(input())

    # buffer가 있는 data_list 
    data_list = []
    for _ in range(100):
        data_list.append([0] + list(map(int, input().split())) + [0])
    data_list.append([0 for _ in range(102)])

    RIGHT = 'right'
    DOWN = 'down'
    LEFT = 'left'

    is_end = False
    for i in range(100):
        i, j = 0, i+1
        start = j-1

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
                    j += 1
                elif direction == LEFT:
                    j -= 1
                else:
                    pass
            
            # 현재 칸이 0이면 멈추고 다음 라인으로
            elif data_list[i][j] == 0:
                break
            # 현재 칸이 2이면 도착
            elif data_list[i][j] == 2:
                is_end = True
                break
            else:
                break
        # is_end가 True이면 정답을 출력하고, 다음 Test Case로 이동
        if is_end == True:
            break
    print(f'#{T} {start}')