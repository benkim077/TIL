import sys

sys.stdin = open(r"input.txt", "r")

T = 10

for t in range(1, T+1):
    w = int(input())
    my_list = list(map(int, input().split()))

    total = 0
    for i in range(2, w - 2):
        max_value = max([my_list[i-2], my_list[i-1], my_list[i+1], my_list[i+2]])
        if my_list[i] - max_value > 0:
            total += my_list[i] - max_value
    print(f'#{t} {total}')
