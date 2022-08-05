my_list = [[1, 3, 3, 6, 7], [8, 13, 9, 12, 8], [4, 16, 11, 12, 6], [2, 4, 1, 23, 2], [9, 13, 4, 7, 3]]

t = int(input())
n, m = map(int, input().split())

for i in range(1, t+1):
    my_list = []
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
        print('<<<', temp)

        if rlt >= temp:
            pass
        else:
            rlt = temp

print(f'#{i} {rlt}')
