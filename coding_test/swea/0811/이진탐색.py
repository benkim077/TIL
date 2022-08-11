import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    P, A, B = tuple(map(int, input().split()))


    # 초기값 및 첫 번째 탐색
    al, ac, ar = 1, int((1+P)/2), P
    bl, bc, br = 1, int((1+P)/2), P
    
    # 이진탐색
    ans = 0
    while ac != A and bc != B:
        # A
        if ac < A:
            al = ac
            ac = int((al + ar)/2)
        elif ac > A:
            ar = ac
            ac = int((al + ar)/2)

        # B
        if bc < B:
            bl = bc
            bc = int((bl + br)/2)
        elif bc > B:
            br = bc
            bc = int((bl + br)/2)

    # 누가 먼저 도달하지?
    if ac == A and bc != B:
        ans = 'A'
    elif ac != A and bc == B:
        ans = 'B'
    else:
        ans = 0

    # 출력
    print(f'#{tc} {ans}')