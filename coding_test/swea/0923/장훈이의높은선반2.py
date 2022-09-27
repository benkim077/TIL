import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())    # 점원 수, 선반 높이
    data = list(map(int, input().split()))
    data.sort(reverse=True)
    sm = 0
    for i in range(N):
        if sm >= B:
            break

        temp_i = sm + data[i]
        if temp_i > B:
            if i + 1 < N:
                for j in range(i + 1, N):
                    temp_j = sm + data[j]
                    if temp_j > B:
                        break
                    elif temp_j == B:
                        sm += data[j]
                        break
                    elif temp_j < B:
                        sm += data[i]
                        break
                # else:
                #     sm += data[j]
            else:
                sm += data[i]
                break
        elif temp_i == B:
            sm += data[i]
            break
        elif temp_i < B:
            sm += data[i]
            continue


        # temp = 0
        # for j in range(i, N):
        #     if sm + data[j] >= B:
        #         if temp > data[j]:
        #             temp = data[j]
        #         continue
        #     else:
        #         sm += data[j]
        #         print(sm, end=' ')
        #         break

    print(f'#{tc} {sm - B}')


