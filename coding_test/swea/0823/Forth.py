# 우선순위를 판단해서 사용해보자(확장)
import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T + 1):
    data = input().split()
    stk = []
    for char in data:
        if char.isdigit():
            stk.append(int(char))
        else:
            if char == '.':
                if len(stk) != 1:
                    ans = 'error'
                    break
                else:
                    ans = stk.pop()
            else:
                if len(stk) < 2:
                    ans = 'error'
                    break
                right = stk.pop()
                left = stk.pop()
                if char == '+':
                    stk.append(left + right)
                elif char == '-':
                    stk.append(left - right)
                elif char == '*':
                    stk.append(left * right)
                else:   # / 인 경우
                    stk.append(left // right)

    print(f'#{tc} {ans}')
