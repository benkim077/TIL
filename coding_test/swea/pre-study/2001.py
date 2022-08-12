import sys

sys.stdin = open(r"input.txt", "r")

T = int(input())

for t in range(1, T+1):
    my_list = []
    n, m = map(int, input().split())
    for _ in range(n):
        my_list.append(list(map(int, input().split())))

    rlt = 0
    # 이동
    for k in range(n - m + 1):
        for j in range(n - m + 1):
            temp = 0
            # 내려침
            for x in range(m):
                for y in range(m):
                    temp += my_list[x+k][y+j]

            # 비교
            if rlt >= temp:
                pass
            else:
                rlt = temp

    print(f'#{t} {rlt}')
