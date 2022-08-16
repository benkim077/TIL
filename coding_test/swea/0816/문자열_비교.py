def is_in(string1, string2):
    for i in range(len(string2) - len(string1) + 1):
        if string1 == string2[i:i + len(string1)]:
            return 1
        else:
            pass
    return 0


T = int(input())

for tc in range(1, T + 1):
    st1 = input()
    st2 = input()

    ans = is_in(st1, st2)

    print(f'#{tc} {ans}')
