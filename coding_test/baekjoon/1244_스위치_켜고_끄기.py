def change_state(idx):
    if lst[idx] == 0:
        lst[idx] = 1
    else:
        lst[idx] = 0
    
    return None

N = int(input())
lst = list(map(int, input().split()))
S = int(input())

for _ in range(S):
    mw, i = map(int, input().split())

    temp = i - 1 # i번 스위치 -> i-1번 인덱스
    # MAN
    if mw == 1:
        while temp < N:
            # ON -> OFF
            if lst[temp] == 1:
                change_state(temp)
            else:
                change_state(temp)
            temp += i

    # WOMAN
    else:
        k = 1 # woman left, right 양옆 확인용 변수
        
        # 중앙은 항상 상태 바꿈
        change_state(temp)

        # 양 옆이 같으면 바꿈
        while temp - k >= 0 and temp + k < N:  # 0번 스위치보다 낮아지면 안 되고, N 보다 커지면 안 된다.
            if lst[temp - k] == lst[temp + k]:  # 같은 거리에 있는 왼쪽 오른쪽을 확인
                change_state(temp - k)
                change_state(temp + k)
                k += 1
            else:
                break

# 출력
for i in range(len(lst)):
    if i % 20 == 0 and i != 0:
        print()
    print(lst[i], end=' ')
