T = 10

for t in range(1, T + 1):
    dump = int(input())
    box_list = list(map(int, input().split()))
    # 덤프 순회
    for _ in range(dump):
        # 최대값의 인덱스를 찾고, 그 자리의 값을 -1
        box_list[box_list.index(max(box_list))] -= 1
        # 최소값의 인덱스를 찾고, 그 자리의 값을 +1
        box_list[box_list.index(min(box_list))] += 1
    # 출력
    print(f'#{t} {max(box_list) - min(box_list)}')