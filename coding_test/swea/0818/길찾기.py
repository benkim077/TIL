import sys
sys.stdin = open('input.txt')


def dfs(start):
    stk = []

    v = start
    vst[v] = 1
    while True:
        w = is_adj(v)
        # 갈 곳이 없는 경우
        if w == -1:
            if stk:
                v = stk.pop()
                continue
            else:
                break
        # 갈 곳이 있는 경우
        else:
            stk.append(v)
            v = w
            vst[w] = 1
            continue


# 정점 번호를 입력하면 어디로 이동해야 하는지 알려주는 함수.
# 리턴이 -1이면 이동할 곳이 없는 것.
# else, 이동할 정점 number 리턴
def is_adj(v):
    if lst1[v] != 0 and vst[lst1[v]] == 0:
        return lst1[v]
    elif lst2[v] != 0 and vst[lst2[v]] == 0:
        return lst2[v]
    else:
        return -1


T = 10
for _ in range(1, T + 1):
    tc, E = map(int, input().split())
    # V(정점 갯수) 어떻게 구하지? 
    # 일단 없어도 될 것 같은데

    # 입력, 데이터 저장
    lst1 = [0] * 100
    lst2 = [0] * 100
    vst = [0] * 100
    data = list(map(int, input().split()))
    for i in range(len(data)):
        if i % 2 == 0:
            idx = data[i]
        else:
            value = data[i]
            if lst1[idx] == 0:
                lst1[idx] = value
            else:
                lst2[idx] = value

    # 0번 인덱스(시작점)부터 99를 갈 수 있는지 탐색
    dfs(0)

    # 출력
    if vst[99] == 1:
        ans = 1
    else:
        ans = 0
    print(f'#{tc} {ans}')
