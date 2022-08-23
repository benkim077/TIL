import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    data = list(input())

    tmp = []    # 최근 연산자가 * 이었으면 빼서 묶고 다시 넣는 스택
    # *곱하기 먼저 처리
    for i in range(len(data)):
        # 무조건 스택에 넣는다
        # 숫자일 때, i-1의 연산자가 *이면 묶어서 다시 스택에 넣는다. (3*3을 33*로 묶는다는 뜻)
        # + 연산은 모든 * 연산이 끝난 후에 한다. 방식은 *와 같다.
        if data[i] != '+' and data[i] != '*':   # 숫자인 경우
            if data[i - 1] == '*':                  # *가 직전인 경우
                oper = tmp.pop()
                left = tmp.pop()
                tmp.append(left + data[i] + oper)
            else:
                tmp.append(data[i])
        else:                                   # + * 인 경우
            tmp.append(data[i])

    # +더하기 처리
    stk = []   # * 작업을 마치고 + 작업을 위해서 사용하는 스택
    for i in range(len(tmp)):
        if tmp[i - 1] == '+':
            oper = stk.pop()
            left = stk.pop()
            stk.append(left + tmp[i] + oper)
        else:
            stk.append(tmp[i])

    ans = ''.join(stk)
    print(f'#{tc} {ans}')
