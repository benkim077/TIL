import sys
sys.stdin = open('input.txt')


while True:
    data_st = input()
    stk = []
    ans = ''

    if len(data_st) == 1 and data_st[0] == '.':
        break

    for char in data_st:
        if char == '(' or char == '[':
            stk.append(char)

        elif char == ')':
            if stk and stk[-1] == '(':
                stk.pop()
            else:
                ans = 'no'
                break

        elif char == ']':
            if stk and stk[-1] == '[':
                stk.pop()
            else:
                ans = 'no'
                break

        elif char == '.':
            if not stk:
                ans = 'yes'
            else:
                ans = 'no'

        else:
            pass

    print(ans)
