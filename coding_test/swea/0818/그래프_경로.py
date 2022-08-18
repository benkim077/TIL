import sys
sys.stdin = open('input.txt')


def is_linked(s, g):
    # dfs
    stk = []
    vst = [0] * (V + 1)

    v = s
    vst[v] = 1
    while True:
        for w in range(V + 1):
            if adj[v][w] == 1 and vst[w] == 0:
                stk.append(v)
                v = w
                vst[w] = 1
                # 여기에 해야 할 일을 적어준다.
                if w == g:
                    return 1
                break
        else:
            if stk:
                v = stk.pop()
            else:
                return 0


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj = list([0] * (V + 1) for _ in range(V + 1))
    for _ in range(E):
        i, j = map(int, input().split())
        adj[i][j] = 1

    start, goal = map(int, input().split())
    ans = is_linked(start, goal)

    print(f'#{tc} {ans}')
