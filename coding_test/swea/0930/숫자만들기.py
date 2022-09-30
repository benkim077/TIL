import sys
sys.stdin = open('input.txt')


operator_dict = {
    0: '+',
    1: '-',
    2: '*',
    3: '//',
}


def get_operator_lst(operator_cnt_lst):
    operator_lst = [0] * (N - 1)
    temp = 0
    for i in range(4):
        k = operator_cnt_lst[i] # 어떤 연산자가 k개 만큼 있으면
        for j in range(temp, temp + k):
            operator_lst[j] = operator_dict[i]
        temp += k
    return operator_lst


# 백트래킹에서 얻은 연산자 순서로 값을 계산해준다.
def solve(opertor_order_lst):
    ret = data_lst[0]
    for i in range(1, N):
        if opertor_order_lst[i - 1] == '+':
            ret += data_lst[i]
        elif opertor_order_lst[i - 1] == '-':
            ret -= data_lst[i]
        elif opertor_order_lst[i - 1] == '*':
            ret *= data_lst[i]
        elif opertor_order_lst[i - 1] == '//':
            if ret >= 0:
                ret //= data_lst[i]
            else:
                ret //= data_lst[i]
                ret += 1
    return ret


# k번째 연산자를 정하는 함수
def bt(k, order_lst):
    global mn, mx

    # 가지치기


    # 종료 조건
    if k == N - 1:
        # 연산자 순서로 수식 계산
        rlt = solve(order_lst)
        # print(order_lst, rlt)

        # 계산 결과로 최소, 최대 갱신
        if rlt < mn:
            mn = rlt
        if rlt > mx:
            mx = rlt
        return
    
    # 하부 함수
    prev = 0
    print(order_lst)
    for i in range(N - 1):
        if i >= 1 and operator_lst[i] == operator_lst[prev]:
            print('다음으로')
            continue

        if not check[i]:
            check[i] = 1
            bt(k + 1, order_lst + [operator_lst[i]])
            check[i] = 0

        prev = i


T = int(input())
for tc in range(1, T + 1):
    N = int(input())    # 숫자의 갯수
    operator_cnt_lst = list(map(int, input().split()))  # 연산자 카운트 리스트를 입력받아
    operator_lst = get_operator_lst(operator_cnt_lst)   # 연산자 리스트를 만듬
    check = [0] * (N - 1)                               # 연산자 사용 체크 리스트

    data_lst = list(map(int, input().split()))
    mx = -100_000_000
    mn = 100_000_000
    bt(0, [])   # 0번째 연산자부터 정하자
    print(f'#{tc} {mx - mn}')