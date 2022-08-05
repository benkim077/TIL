t = int(input())

for i in range(1, t+1):
    my_list = []
    n, m = map(int, input().split())
    for _ in range(n):
        my_list.append(list(map(int, input().split())))

    rlt = 0
    for k in range(len(my_list) - m + 1):
        for j in range(len(my_list) - m + 1):
            temp = 0
            # 계산
            for x in range(m):
                for y in range(m):
                    temp += my_list[x+k][y+j]

            if rlt >= temp:
                pass
            else:
                rlt = temp
    print('<<<', temp)

