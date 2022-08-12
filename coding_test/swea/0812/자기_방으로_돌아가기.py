import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    lst = [0] * 400

    N = int(input())

    for _ in range(N):
        start, end = tuple(map(int, input().split()))

        # start, end 위치 조절
        if start == end:
            continue
        elif start < end:
            if start % 2 == 0:
                new_start = start - 1
            else:
                new_start = start
            if end % 2 == 0:
                new_end = end
            else:
                new_end = end + 1
        elif start > end:
            if start % 2 == 0:
                new_start = start
            else:
                new_start = start + 1
            if end % 2 == 0:
                new_end = end - 1
            else:
                new_end = end
        # 한 사람의 동선을 +1로 표시
        if start < end:
            for i in range(new_start - 1, new_end):
                lst[i] += 1
        elif start > end:
            for i in range(new_start - 1, new_end, -1):
                lst[i] += 1
    # 최댓값 구하기
    mx = 0
    for j in range(len(lst)):
        if mx < lst[j]:
            mx = lst[j]

    # 출력
    print(f'#{tc} {mx}')

