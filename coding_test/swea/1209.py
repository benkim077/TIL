import sys

sys.stdin = open(r"input.txt","r")


for _ in range(10):
    # 몇 번째 테스트?
    T = int(input())
    # 2차원 배열 입력
    my_list = []
    for _ in range(100):
        my_list.append(list(map(int, input().split())))
    
    # 가로 total
    total_list = []
    for i in range(100):
        total_list.append(sum(my_list[i]))
    # 세로 total
    for i in range(100):
        total = 0
        for j in range(100):
            total += my_list[j][i]
        total_list.append(total)
    # / total
    for i in range(100):
        total = 0
        total += my_list[i][99-i]
    total_list.append(total)
    # \ total
    for i in range(100):
        total = 0
        total += my_list[i][i]
    total_list.append(total)
    # 최대값 출력
    print(f'#{T} {max(total_list)}')