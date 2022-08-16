import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    str1, str2 = input().split()

    # str2가 더 긴 경우는 str1을 다 쳐야함
    if len(str1) < len(str2):
        ans = len(str1)
    # str1가 더 긴 경우, 중복되는 문자열 센다. (cnt)
    else:
        i = 0
        cnt = 0
        while i < len(str1) - len(str2) + 1:
            # 포함?
            if str1[i:i + len(str2)] == str2:
                cnt += 1
                i += len(str2)
            else:
                i += 1

        # 길이 k 인 문자열이 n 번 중복된다면,
        # n * (k - 1)번 줄일 수 있다.
        ans = len(str1) - (cnt * (len(str2) - 1))

    # 출력
    print(f'#{tc} {ans}')
