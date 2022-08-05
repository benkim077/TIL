my_list = [1, 700, 3, 4,356,341,1,1111]

m = int(input())

rlt = 0

# 어디서 계산?
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


    # temp = 0
    # 이제 계산
    # for i in range(m):
    #     temp += my_list[i+k] 
    # print('<<<', temp)
    
    # if rlt >= temp:
    #     pass
    # else:
    #     rlt = temp

print(rlt)
